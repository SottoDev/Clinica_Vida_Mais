
from db import criar_db
from menu import exibir_menu, exibir_mensagem_saida, exibir_mensagem_boas_vindas
from paciente import (
    cadastrar_paciente,
    exibir_estatisticas,
    buscar_paciente,
    listar_pacientes,
    deletar_paciente
)


def main():

    exibir_mensagem_boas_vindas()

    criar_db()
    

    while True:
        escolha = exibir_menu()
        
        if escolha == 1:
            cadastrar_paciente()
        
        elif escolha == 2:
            exibir_estatisticas()
        
        elif escolha == 3:
            buscar_paciente()
        
        elif escolha == 4:
            listar_pacientes()
        
        elif escolha == 5:
            deletar_paciente()
        
        elif escolha == 6:
            exibir_mensagem_saida()
            break
        
        else:
            print(" Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()