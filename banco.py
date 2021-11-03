#!/usr/bin/env python3

import sqlite3

class Banco:
    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()

    def inserir_despesa(self, data, descricao, valor):
        consulta = 'INSERT OR IGNORE INTO despesas (data, descricao, valor) VALUES ( ?, ?, ?)'
        self.cursor.execute(consulta, (data, descricao, valor))
        self.conn.commit()

    def editar_despesa(self, data, descricao, valor, id):
       consulta = 'UPDATE OR IGNORE despesas SET data=?, descricao=?, valor=? WHERE id=?'
       self.cursor.execute(consulta, (data, descricao, valor, id))
       self.conn.commit()

    def excluir_despesa(self, id):
        consulta = 'DELETE FROM despesas WHERE id=?'
        self.cursor.execute(consulta, (id,))
        self.conn.commit()

    # Não será impresso em linha de comando, portanto é necessário refatorar essa função.
    def listar_despesas(self):
        self.cursor.execute('SELECT * FROM despesas')
        for linha in self.cursor.fetchall():
            print(linha)

    def fechar(self):
        self.cursor.close()
        self.conn.close()
