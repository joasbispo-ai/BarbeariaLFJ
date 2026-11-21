from cadastro import cadastrar_agendamento
from consultas import listar_todos, consultar_individual
from atualizacoes import atualizar_agendamento
from exclusoes import excluir_agendamento

def exibir_menu():
    while True:
        print("\n==========================================")
        print("      SISTEMA DE GESTÃO - BARBEARIA LFJ   ")
        print("==========================================")
        print("1 - Cadastrar novo agendamento (Create)")
        print("2 - Listar todos os agendamentos (Read)")
        print("3 - Buscar agendamento específico (Read)")
        print("4 - Atualizar agendamento (Update)")
        print("5 - Excluir agendamento (Delete)")
        print("0 - Sair do sistema")
        print("==========================================")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_agendamento()
        elif opcao == "2":
            listar_todos()
        elif opcao == "3":
            consultar_individual()
        elif opcao == "4":
            atualizar_agendamento()
        elif opcao == "5":
            excluir_agendamento()
        elif opcao == "0":
            print("\nEncerrando o sistema da Barbearia LFJ. Até logo!")
            break
        else:
            print("\nOpção inválida! Digite um número entre 0 e 5.")

if __name__ == "__main__":
    exibir_menu()