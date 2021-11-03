#!/usr/bin/env python3

import sqlite3

class Banco:
    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()

    def fechar(self):
        self.cursor.close()
        self.conn.close()
