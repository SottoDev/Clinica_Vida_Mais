def exibir_menu():

    print("\n" + "="*40)
    print("=== SISTEMA CLÍNICA VIDA+ ===")
    print("="*40)
    print("1. Cadastrar paciente")
    print("2. Ver estatísticas")
    print("3. Buscar paciente")
    print("4. Listar todos os pacientes")
    print("5. Deletar paciente")
    print("6. Sair")
    print("="*40)
    
    try:
        escolha = int(input("Escolha uma opção: "))
        return escolha
    except ValueError:
        print("Digite um número válido!")
        return 0


def exibir_mensagem_saida():
    """
    Exibe mensagem de encerramento
    """
    print("\n" + "="*40)
    print("Encerrando o programa...")
    print("Obrigado por usar o Sistema Clínica Vida+")
    print("="*40)
    print("Programa finalizado.")


def exibir_mensagem_boas_vindas():
 
    print("\n" + "="*40)
    print("BEM-VINDO AO SISTEMA CLÍNICA VIDA+")
    print("="*40)
    print("Sistema de gerenciamento de pacientes")
    print("Versão 1.0")
    print("="*40)