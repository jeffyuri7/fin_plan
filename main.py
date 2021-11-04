#!/usr/bin/env python3

from banco import Banco
from resumo import Resumo
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Manipulador:
    def __init__(self):
        self.armazenamento: Gtk.ListStore = builder.get_object('liststore1')
        self.Stack: Gtk.Stack = builder.get_object('stack')
        self.banco = Banco('bancodedados.db')

    def on_main_window_destroy(self, window):
        Gtk.main_quit()

    def on_btn_inserir_orcamento_clicked(self, button):
        orcamento = builder.get_object('ent_valor_disp').get_text()
        self.atualizar_orcamento(orcamento)

    def atualizar_orcamento(self, orcamento):
        resumo = Resumo(self.banco)
        print(resumo.saldo_dia)


builder = Gtk.Builder()
builder.add_from_file('ui.glade')
builder.connect_signals(Manipulador())
window = builder.get_object('main_window')
window.show_all()
Gtk.main()
