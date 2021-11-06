#!/usr/bin/env python3

from banco import Banco
from resumo import Resumo
from despesas import Despesa, ListaDespesa
import gi
from datetime import date
import calendar

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Manipulador:
    def __init__(self):
        # Inicializador do Manipulador. Os dados de resumo e a lista de despesas são inicializadas e escritas na tela neste momento.
        self.armazenamento: Gtk.ListStore = builder.get_object('liststore1')
        self.Stack: Gtk.Stack = builder.get_object('stack')
        self.banco = Banco('bancodedados.db')
        self.atualizar_tela()

    def on_main_window_destroy(self, window):
        # Função para fechar a aplicação quando clicar no X da janela
        self.banco.fechar()
        Gtk.main_quit()

    def mes_atual(self):
        # Uma função que retorna uma tupla com o dia atual e o último dia do mês ambos como int
        data = date.today()
        hoje = int(data.strftime('%d'))
        ultimo_dia = calendar.monthrange(int(data.strftime('%Y')), int(data.strftime('%m')))[1]
        return hoje, ultimo_dia

    def atualizar_tela(self):
        # Consulta o banco de dados e cria dois objetos: um resumo e uma lista de despesas
        self.resumo = Resumo(self.banco)
        self.lista_despesas = ListaDespesa(self.banco).lista_de_dados
        self.calcular_dados()
        self.formatar_dados()

    def calcular_dados(self):
        # Calcula os dados de lista para atualizar o resumo
        soma_despesas = 0
        for despesa in self.lista_despesas:
           soma_despesas += despesa[3]
        saldo_restante = self.resumo.saldo_disponivel - soma_despesas
        periodo = self.mes_atual()
        dias_restantes = (periodo[1] - periodo[0]) + 1
        media_por_dia = saldo_restante / dias_restantes

        return soma_despesas, saldo_restante, media_por_dia

    def formatar_dados(self):
        # Atualiza a tela com os dados que foram buscados do BD.
        builder.get_object('lbl_valor_gasto_realizado').set_text(str(f'R$ {self.resumo.gasto:.2f}').replace('.',','))
        builder.get_object('lbl_saldo_restante').set_text(str(f'R$ {self.resumo.saldo_dia:.2f}').replace('.',','))
        builder.get_object('lbl_media_por_dia').set_text(str(f'R$ {self.resumo.media_dia:.2f}').replace('.',','))
        builder.get_object('lbl_orcamento_previsto').set_text(str(f'R$ {self.resumo.saldo_disponivel:.2f}').replace('.',','))
        self.armazenamento.clear()
        for despesa in self.lista_despesas:
            self.armazenamento.append((despesa[1], despesa[2], str(f'R$ {despesa[3]:.2f}').replace('.',',')))


    # Funções referentes aos pressionamentos de botões

    def on_btn_inserir_orcamento_clicked(self, button):
        # Função que permite inserir um valor para o orçamento desejado do mês
        orcamento = builder.get_object('ent_valor_disp').get_text()
        self.resumo.atualizar_orcamento(float(orcamento), 1)
        self.atualizar_tela()
        builder.get_object('ent_valor_disp').set_text('')

    def on_btn_adicionar_clicked(self, button):
        # Função para abrir a tela Adicionar Despesa
        self.Stack.set_visible_child_name('view_adicionar')
        builder.get_object('ent_data').grab_focus()

    def on_btn_cancelar_clicked(self, button):
        # Função para retornar da tela Adicionar Despesa para a tela principal do software
        self.Stack.set_visible_child_name('view_principal')

    def on_btn_adicionar_confirmar_clicked(self, button):
        # Função para confirmar e commitar uma nova despesa. Após isso, os dados são atualizados
        builder.get_object('ent_data').grab_focus()
        data = builder.get_object('ent_data').get_text()
        descricao = builder.get_object('ent_descricao').get_text()
        valor = float(builder.get_object('ent_valor').get_text())
        nova_despesa = Despesa(self.banco, data, descricao, valor)
        nova_despesa.inserir_despesa()
        builder.get_object('ent_data').set_text('')
        builder.get_object('ent_descricao').set_text('')
        builder.get_object('ent_valor').set_text('')
        self.atualizar_tela()
        self.Stack.set_visible_child_name('view_principal')


    def on_btn_editar_clicked(self):
        # Função para editar uma despesa que já está no BD
        pass

    def on_btn_excluir_clicked(self, button):
        # Função para excluir uma despesa que já está no BD
        selecao = builder.get_object('treeview_princ').get_selection()
        selecao.connect("changed", on_tree_selection_changed)

    def on_tree_selection_changed(self, selection):
        # Função para obter os dados selecionados de uma treeview
        model, treeiter = selection.get_selected()
        if treeiter is not None:
            print('Você selecionou', model[treeiter][0])

    def on_btn_zerar_clicked(self):
        # Função para zerar os dados do BD. Útil para iniciar um novo mês com um novo orçamento
        pass

builder = Gtk.Builder()
builder.add_from_file('ui.glade')
builder.connect_signals(Manipulador())
window = builder.get_object('main_window')
window.show_all()
Gtk.main()
