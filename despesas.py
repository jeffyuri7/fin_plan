#!/usr/bin/env python3

class Despesa:
    def __init__(self, data, descricao, valor):
        self.data = data
        self.descricao = descricao
        self.valor = valor

    def inserir_despesa(self, despesa):
        consulta = 'INSERT OR IGNORE INTO despesas (data, descricao, valor) VALUES ( ?, ?, ?)'
        self.cursor.execute(consulta, (self.data, self.descricao, self.valor))
        self.conn.commit()

    def editar_despesa(self, id):
       consulta = 'UPDATE OR IGNORE despesas SET data=?, descricao=?, valor=? WHERE id=?'
       self.cursor.execute(consulta, (self.data, self.descricao, self.valor, id))
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
