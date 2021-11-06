#!/usr/bin/env python3

from banco import Banco
from resumo import Resumo
from despesas import Despesa
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Manipulador:
    def __init__(self):
        self.armazenamento: Gtk.ListStore = builder.get_object('liststore1')
        self.Stack: Gtk.Stack = builder.get_object('stack')
        self.banco = Banco('bancodedados.db')
        self.atualizar_orcamento()
        self.atualizar_lista_de_despesas()

    def on_main_window_destroy(self, window):
        Gtk.main_quit()

    def on_btn_inserir_orcamento_clicked(self, button):
        orcamento = builder.get_object('ent_valor_disp').get_text()
        self.atualizar_orcamento(orcamento)

    def atualizar_orcamento(self):
        resumo = Resumo(self.banco)
        builder.get_object('lbl_valor_gasto_realizado').set_text(str(f'R$ {resumo.gasto:.2f}').replace('.',','))
        builder.get_object('lbl_saldo_dia').set_text(str(f'R$ {resumo.saldo_dia:.2f}').replace('.',','))
        builder.get_object('lbl_media_por_dia').set_text(str(f'R$ {resumo.media_dia:.2f}').replace('.',','))
        builder.get_object('lbl_valor_saldo_disp').set_text(str(f'R$ {resumo.saldo_disponivel:.2f}').replace('.',','))

    def atualizar_lista_de_despesas(self):
        lista_despesas = Despesa(self.banco).lista_de_dados
        self.armazenamento.clear()
        for despesa in lista_despesas:
            self.armazenamento.append((despesa[1], despesa[2], str(f'R$ {despesa[3]:.2f}').replace('.',',')))

builder = Gtk.Builder()
builder.add_from_file('ui.glade')
builder.connect_signals(Manipulador())
window = builder.get_object('main_window')
window.show_all()
Gtk.main()
