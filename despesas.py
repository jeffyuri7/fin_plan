#!/usr/bin/env python3

from banco import Banco

class ListaDespesa:
    # Uma classe para gerar um objeto ListaDespesa para ser utilizado na GUI
    def __init__(self, banco):
        self.banco = banco
        self.lista_de_dados = self.listar_despesas()

    # Não será impresso em linha de comando, portanto é necessário refatorar essa função.
    def listar_despesas(self):
        lista_despesas = []
        self.banco.cursor.execute('SELECT * FROM despesas')
        for linha in self.banco.cursor.fetchall():
            lista_despesas.append(linha)
        return lista_despesas

    def editar_despesa(self, identificador):
       consulta = 'UPDATE OR IGNORE despesas SET data=?, descricao=?, valor=? WHERE id=?'
       self.banco.cursor.execute(consulta, (self.data, self.descricao, self.valor, id))
       self.banco.conn.commit()

    def excluir_despesa(self, identificador):
        consulta = 'DELETE FROM despesas WHERE id=?'
        self.banco.cursor.execute(consulta, (identificador,))
        self.banco.conn.commit()


class Despesa:
    # Uma classe para adicionar novos objetos Despesa no banco de dados
    def __init__(self, banco, data, descricao, valor):
        self.banco = banco
        self.data = data
        self.descricao = descricao
        self.valor = valor

    def inserir_despesa(self):
        consulta = 'INSERT OR IGNORE INTO despesas (data, descricao, valor) VALUES ( ?, ?, ?)'
        self.banco.cursor.execute(consulta, (self.data, self.descricao, self.valor))
        self.banco.conn.commit()

    """Para editar uma despesa crie uma nova despesa e chame o método editar despesa passando o id da
    despesa que deverá ser alterado como argumento. Na gui deve ser criado um objeto Despesa com os dados
    da atualização e em vez de solicitar a inserção da despesa, vou solicitar a edição da despesa passando
    o id como argumento."""

if __name__ == '__main__':
    despesa1 = Despesa(Banco('bancodedados.db'))
    print(despesa1.lista_de_dados)
    #despesa1.editar_despesa(4)
    #despesa1.listar_despesas()
