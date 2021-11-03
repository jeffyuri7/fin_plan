#!/usr/bin/env python3

from banco import Banco

class Despesa:
    def __init__(self, data, descricao, valor):
        self.data = data
        self.descricao = descricao
        self.valor = valor
        self.banco = Banco('bancodedados.db')

    def inserir_despesa(self):
        consulta = 'INSERT OR IGNORE INTO despesas (data, descricao, valor) VALUES ( ?, ?, ?)'
        self.banco.cursor.execute(consulta, (self.data, self.descricao, self.valor))
        self.banco.conn.commit()

    def editar_despesa(self, id):
       consulta = 'UPDATE OR IGNORE despesas SET data=?, descricao=?, valor=? WHERE id=?'
       self.banco.cursor.execute(consulta, (self.data, self.descricao, self.valor, id))
       self.banco.conn.commit()

    def excluir_despesa(self, id):
        consulta = 'DELETE FROM despesas WHERE id=?'
        self.banco.cursor.execute(consulta, (id,))
        self.banco.conn.commit()

    # Não será impresso em linha de comando, portanto é necessário refatorar essa função.
    def listar_despesas(self):
        self.banco.cursor.execute('SELECT * FROM despesas')
        for linha in self.banco.cursor.fetchall():
            print(linha)


if __name__ == '__main__':
    despesa1 = Despesa('06/04/20', 'Carnes', 22.40)
    despesa1.inserir_despesa()
    despesa1.listar_despesas()