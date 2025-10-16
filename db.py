import sqlite3

def criar_db():

    try:
        conexao = sqlite3.connect("clinica.db")
        cursor = conexao.cursor()

        cursor.execute('''
                CREATE TABLE IF NOT EXISTS pacientes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    idade INTEGER NOT NULL,
                    telefone TEXT NOT NULL
                )
            ''')

        conexao.commit()
        conexao.close()

        print("Banco de dados criado")

    except sqlite3.Error as erro:
        print(f"Erro ao criar banco: {erro}")

def obter_conexao():
    try:
        return sqlite3.connect("clinica.db")
    except sqlite3.Error as erro:
        print(f"Erro ao conectar:{erro} ")

def fechar_conexao(conexao):
    if conexao:
        conexao.close()