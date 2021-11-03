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

    """Para editar uma despesa crie uma nova despesa e chame o método editar despesa passando o id da
    despesa que deverá ser alterado como argumento. Na gui deve ser criado um objeto Despesa com os dados
    da atualização e em vez de solicitar a inserção da despesa, vou solicitar a edição da despesa passando
    o id como argumento."""
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
    despesa1 = Despesa('08/04/21', 'Meia', 3.40)
    #despesa1.inserir_despesa()
    #despesa1.editar_despesa(4)
    #despesa1.listar_despesas()