#!/usr/bin/env python3

from banco import Banco
from resumo import Resumo
from despesas import Despesa, ListaDespesa
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Manipulador:
    def __init__(self):
        self.armazenamento: Gtk.ListStore = builder.get_object('liststore1')
        self.Stack: Gtk.Stack = builder.get_object('stack')
        self.banco = Banco('bancodedados.db')
        # Atualiza os dados de resumo e a lista de despesas no momento da abertura do software
        self.atualizar_tela()

    def on_main_window_destroy(self, window):
        self.banco.fechar()
        Gtk.main_quit()

    def atualizar_tela(self):
        self.resumo = Resumo(self.banco)
        builder.get_object('lbl_valor_gasto_realizado').set_text(str(f'R$ {self.resumo.gasto:.2f}').replace('.',','))
        builder.get_object('lbl_saldo_dia').set_text(str(f'R$ {self.resumo.saldo_dia:.2f}').replace('.',','))
        builder.get_object('lbl_media_por_dia').set_text(str(f'R$ {self.resumo.media_dia:.2f}').replace('.',','))
        builder.get_object('lbl_valor_saldo_disp').set_text(str(f'R$ {self.resumo.saldo_disponivel:.2f}').replace('.',','))
        self.lista_despesas = ListaDespesa(self.banco).lista_de_dados
        self.armazenamento.clear()
        for despesa in self.lista_despesas:
            self.armazenamento.append((despesa[1], despesa[2], str(f'R$ {despesa[3]:.2f}').replace('.',',')))

    def on_btn_inserir_orcamento_clicked(self, button):
        orcamento = builder.get_object('ent_valor_disp').get_text()
        #self.atualizar_orcamento(orcamento)

    def on_btn_adicionar_clicked(self, button):
        self.Stack.set_visible_child_name('view_adicionar')
        builder.get_object('ent_data').grab_focus()

    def on_btn_cancelar_clicked(self, button):
        self.Stack.set_visible_child_name('view_principal')

    def on_btn_adicionar_confirmar_clicked(self, button):
        builder.get_object('ent_data').grab_focus()
        data = builder.get_object('ent_data').get_text()
        descricao = builder.get_object('ent_descricao').get_text()
        valor = float(builder.get_object('ent_valor').get_text())
        nova_despesa = Despesa(self.banco, data, descricao, valor)
        nova_despesa.inserir_despesa()
        self.Stack.set_visible_child_name('view_principal')
        builder.get_object('ent_data').set_text('')
        builder.get_object('ent_descricao').set_text('')
        builder.get_object('ent_valor').set_text('')
        self.atualizar_tela()

    def on_btn_editar_clicked(self):
        pass

    def on_btn_excluir_clicked(self, button):
        selecao = builder.get_object('treeview_princ').get_selection()
        selecao.connect("changed", on_tree_selection_changed)

    def on_tree_selection_changed(self, selection):
        model, treeiter = selection.get_selected()
        if treeiter is not None:
            print('Você selecionou', model[treeiter][0])

    def on_btn_zerar_clicked(self):
        pass

builder = Gtk.Builder()
builder.add_from_file('ui.glade')
builder.connect_signals(Manipulador())
window = builder.get_object('main_window')
window.show_all()
Gtk.main()
