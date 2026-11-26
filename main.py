import os
from cadastro import cadastrar_agendamento
from consultas import listar_todos, consultar_individual
from atualizacoes import atualizar_agendamento
from exclusoes import excluir_agendamento

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def exibir_menu():
    mensagem = ""

    while True:
        limpar_tela()
        print("==========================================")
        print("      SISTEMA DE GESTÃO - BARBEARIA LFJ   ")
        print("==========================================")
        print("1 - Cadastrar novo agendamento (Create)")
        print("2 - Listar todos os agendamentos (Read)")
        print("3 - Buscar agendamento específico (Read)")
        print("4 - Atualizar agendamento (Update)")
        print("5 - Excluir agendamento (Delete)")
        print("0 - Sair do sistema")
        print("==========================================")

        if mensagem:
            print(f"\n>> {mensagem}\n")
            mensagem = ""

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            limpar_tela()
            mensagem = cadastrar_agendamento()
        elif opcao == "2":
            limpar_tela()
            listar_todos()
            input("\nPressione ENTER para voltar ao menu...")
        elif opcao == "3":
            limpar_tela()
            consultar_individual()
            input("\nPressione ENTER para voltar ao menu...")
        elif opcao == "4":
            limpar_tela()
            atualizar_agendamento()
            input("\nPressione ENTER para voltar ao menu...")
        elif opcao == "5":
            limpar_tela()
            excluir_agendamento()
            input("\nPressione ENTER para voltar ao menu...")
        elif opcao == "0":
            print("\nEncerrando o sistema da Barbearia LFJ. Até logo!")
            break
        else:
            mensagem = "Opção inválida! Digite um número entre 0 e 5."

if __name__ == "__main__":
    exibir_menu()