#!/usr/bin/env python3

from banco import Banco
import sqlite3

class Resumo:
    def __init__(self, gasto, saldo_dia, media_dia, saldo_disponivel):
        self.gasto = gasto
        self.saldo_dia = saldo_dia
        self.media_dia = media_dia
        self.saldo_disponivel = saldo_disponivel
        self.banco = Banco('bancodedados.db')

    def inserir_resumo(self):
        consulta = 'INSERT OR IGNORE INTO resumo (gasto, saldo_dia, media_dia, saldo_disponivel) VALUES ( ?, ?, ?, ?)'
        self.banco.cursor.execute(consulta, (self.gasto, self.saldo_dia, self.media_dia, self.saldo_disponivel))
        self.banco.conn.commit()

    # Método para atualizar os dados no BD. Haverá apenas uma lista de dados nessa tabela.
    def enviar_resumo(self, id):
        consulta = 'UPDATE OR IGNORE resumo SET gasto=?, saldo_dia=?, media_dia=?, saldo_disponivel=? WHERE id=?'
        self.banco.cursor.execute(consulta, (self.gasto, self.saldo_dia, self.media_dia, self.saldo_disponivel, id))
        self.banco.conn.commit()

    # Método para atualizar o resumo direto no programa, para mostrar na GUI
    def atualizar_resumo(self):
        pass

    def buscar_resumo(self):
        self.banco.cursor.execute('SELECT * FROM resumo WHERE id=1')
        for linha in self.banco.cursor.fetchall():
            print(linha)


if __name__ == '__main__':
    resumo = Resumo(14.5, 43.4, 0.0, 11.11)
    # resumo.inserir_resumo()
    resumo.enviar_resumo(1)
    resumo.buscar_resumo()
