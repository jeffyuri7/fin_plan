#!/usr/bin/env python3

from banco import Banco
import sqlite3

class Resumo:
    # Consulta o BD e cria um objeto Resumo com os últimos dados registrados no banco como seus atributos
    def __init__(self, banco):
        self.banco = banco
        self.banco.cursor.execute('SELECT * FROM resumo WHERE id=1')
        for identificador, gasto, saldo_dia, media_dia, saldo_disponivel in self.banco.cursor.fetchall():
            self.identificador = identificador
            self.gasto = gasto
            self.saldo_dia = saldo_dia
            self.media_dia = media_dia
            self.saldo_disponivel = saldo_disponivel

    def atualizar_orcamento(self, orcamento, identificador):
        consulta = 'UPDATE resumo SET saldo_disponivel=? WHERE id=?'
        self.banco.cursor.execute(consulta, (orcamento, identificador))
        self.banco.conn.commit()

    def inserir_resumo(self, gasto, saldo_dia, media_dia, saldo_disponivel, identificador):
        consulta = 'INSERT OR IGNORE INTO resumo (gasto, saldo_dia, media_dia, saldo_disponivel) VALUES ( ?, ?, ?, ?)'
        self.banco.cursor.execute(consulta, (self.gasto, self.saldo_dia, self.media_dia, self.saldo_disponivel))
        self.banco.conn.commit()

    # Método para atualizar os dados no BD. Haverá apenas uma lista de dados nessa tabela.
    def enviar_resumo(self, gasto, saldo_dia, media_dia, saldo_disponivel, identificador):
        consulta = 'UPDATE resumo SET gasto=?, saldo_dia=?, media_dia=?, saldo_disponivel=? WHERE id=?'
        self.banco.cursor.execute(consulta, (gasto, saldo_dia, media_dia, saldo_disponivel, identificador))
        self.banco.conn.commit()

    # Método para atualizar o resumo direto no programa, para mostrar na GUI
    def atualizar_resumo(self):
        pass

    def buscar_resumo(self):
        self.banco.cursor.execute('SELECT * FROM resumo WHERE id=1')
        for identificador, gasto, saldo_dia, media_dia, saldo_disponivel in self.banco.cursor.fetchall():
            return identificador, gasto, saldo_dia, media_dia, saldo_disponivel


if __name__ == '__main__':
    resumo = Resumo(Banco('bancodedados.db'))
    print(resumo)
    # resumo.inserir_resumo()
    # resumo.enviar_resumo(1)
    # resumo.buscar_resumo()
