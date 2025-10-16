import sqlite3
from db import obter_conexao, fechar_conexao

def cadastrar_paciente():
    print("\n === CADASTRO DE CLIIENTE ===")

    nome = input("Digite o seu nome: ")

    if nome == "":
        print("O campo não pode estar vazio")
        return
    
    try:
        idade = int(input("idade: "))

        if idade < 0  or idade > 199:
            print("A idade deve ser valida")
            return
        
    except ValueError:
        print("Idade deve ser numeros")
        return
    
    telefone = input("Telefone: ")

    if telefone == "":
        print("O telefone não pode estar vazio")
        return
    
    try:
        conexao = obter_conexao()
        cursor = conexao.cursor()
        
        cursor.execute('''
            INSERT INTO pacientes (nome, idade, telefone)
            VALUES (?, ?, ?)
        ''', (nome, idade, telefone))
        
        conexao.commit()
        fechar_conexao(conexao)
        print("Paciente cadastrado")

    except sqlite3.Error as erro:
     print(f"Erro ao cadastras: {erro}")

def exibir_estatisticas():
    print("\n=== ESTATÍSTICAS ===")
    
    try:
        conexao = obter_conexao()
        cursor = conexao.cursor()
        
        cursor.execute('SELECT COUNT(*) FROM pacientes')
        total = cursor.fetchone()[0]
        
        if total == 0:
            print("Nenhum paciente cadastrado!")
            fechar_conexao(conexao)
            return
        
        print(f"Total de pacientes: {total}")

        cursor.execute('SELECT AVG(idade) FROM pacientes')
        idade_media = cursor.fetchone()[0]
        print(f"Idade média: {idade_media:.1f} anos")
        
        cursor.execute('''
            SELECT nome, idade FROM pacientes
            WHERE idade = (SELECT MIN(idade) FROM pacientes)
            LIMIT 1
        ''')
        paciente_novo = cursor.fetchone()
        print(f"Paciente mais novo: {paciente_novo[0]} ({paciente_novo[1]} anos)")
        
        cursor.execute('''
            SELECT nome, idade FROM pacientes
            WHERE idade = (SELECT MAX(idade) FROM pacientes)
            LIMIT 1
        ''')
        paciente_velho = cursor.fetchone()
        print(f"Paciente mais velho: {paciente_velho[0]} ({paciente_velho[1]} anos)")
        
        fechar_conexao(conexao)
        
    except sqlite3.Error as erro:
        print(f"Erro ao buscar estatísticas: {erro}")


def buscar_paciente():

    print("\n=== BUSCAR PACIENTE ===")
    
    nome_procurado = input("Digite o nome do paciente: ")
    
    try:
        conexao = obter_conexao()
        cursor = conexao.cursor()
        
        cursor.execute('''
            SELECT id, nome, idade, telefone FROM pacientes
            WHERE nome LIKE ?
        ''', ('%' + nome_procurado + '%',))
        
        resultados = cursor.fetchall()
        
        if len(resultados) == 0:
            print(" Nenhum paciente encontrado!")
        else:
            print(f"\n {len(resultados)} paciente(s) encontrado(s):")
            for paciente in resultados:
                print(f"\nID: {paciente[0]}")
                print(f"Nome: {paciente[1]}")
                print(f"Idade: {paciente[2]} anos")
                print(f"Telefone: {paciente[3]}")
        
        fechar_conexao(conexao)
        
    except sqlite3.Error as erro:
        print(f" Erro ao buscar paciente: {erro}")


def listar_pacientes():

    print("\n=== LISTA DE PACIENTES ===")
    
    try:
        conexao = obter_conexao()
        cursor = conexao.cursor()
        
        cursor.execute('SELECT id, nome, idade, telefone FROM pacientes ORDER BY nome')
        pacientes = cursor.fetchall()
        
        if len(pacientes) == 0:
            print("Nenhum paciente cadastrado!")
            fechar_conexao(conexao)
            return
        
        for numero, paciente in enumerate(pacientes, start=1):
            print(f"\n{numero}. {paciente[1]}")
            print(f"   ID: {paciente[0]}")
            print(f"   Idade: {paciente[2]} anos")
            print(f"   Telefone: {paciente[3]}")
        
        fechar_conexao(conexao)
        
    except sqlite3.Error as erro:
        print(f"Erro ao listar pacientes: {erro}")


def deletar_paciente():

    print("\n=== DELETAR PACIENTE ===")
    
    try:
        conexao = obter_conexao()
        cursor = conexao.cursor()

        cursor.execute('SELECT id, nome FROM pacientes ORDER BY nome')
        pacientes = cursor.fetchall()
        
        if len(pacientes) == 0:
            print("Nenhum paciente cadastrado!")
            fechar_conexao(conexao)
            return
        
        print("\nPacientes cadastrados:")
        for paciente in pacientes:
            print(f"ID {paciente[0]}: {paciente[1]}")
        
        try:
            id_deletar = int(input("\nDigite o ID do paciente a deletar (0 para cancelar): "))
            
            if id_deletar == 0:
                print("Operação cancelada.")
                fechar_conexao(conexao)
                return
            
            cursor.execute('DELETE FROM pacientes WHERE id = ?', (id_deletar,))
            
            if cursor.rowcount == 0:
                print("ID não encontrado!")
            else:
                conexao.commit()
                print("Paciente deletado com sucesso!")
        
        except ValueError:
            print("ID deve ser um número!")
        
        fechar_conexao(conexao)
        
    except sqlite3.Error as erro:
        print(f"Erro ao deletar paciente: {erro}")