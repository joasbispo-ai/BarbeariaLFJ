from mysql.connector import Error
from conexao import conectar
from validacoes import ler_id_valido, ler_texto_obrigatorio, ler_valor_monetario

def atualizar_agendamento():
    print("\n--- ATUALIZAR AGENDAMENTO ---")
    id_agendamento = ler_id_valido("Informe o ID do agendamento que deseja alterar: ")

    conn = conectar()
    if not conn:
        return

    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM agendamentos WHERE id = %s", (id_agendamento,))
        registro = cursor.fetchone()

        if not registro:
            print(f"Nenhum agendamento encontrado com o ID {id_agendamento}.")
            return

        print(f"\nRegistro atual: {registro['cliente_nome']} - {registro['servico']} ({registro['data_horario']}) - Status: {registro['status']}")
        print("O que deseja atualizar?")
        print("1 - Data e Horário")
        print("2 - Serviço e Valor")
        print("3 - Status (ex: Concluído, Cancelado, Agendado)")
        escolha = input("Opção: ").strip()

        if escolha == "1":
            nova_data = ler_texto_obrigatorio("Nova data e horário: ")
            cursor.execute("UPDATE agendamentos SET data_horario = %s WHERE id = %s", (nova_data, id_agendamento))
        elif escolha == "2":
            novo_servico = ler_texto_obrigatorio("Novo serviço: ")
            novo_valor = ler_valor_monetario("Novo valor (R$): ")
            cursor.execute("UPDATE agendamentos SET servico = %s, valor = %s WHERE id = %s", (novo_servico, novo_valor, id_agendamento))
        elif escolha == "3":
            novo_status = ler_texto_obrigatorio("Novo status: ")
            cursor.execute("UPDATE agendamentos SET status = %s WHERE id = %s", (novo_status, id_agendamento))
        else:
            print("Opção inválida. Nenhuma alteração realizada.")
            return

        conn.commit()
        print("Agendamento atualizado com sucesso!")
    except Error as erro:
        print(f"\nErro ao atualizar registro: {erro}")
    finally:
        cursor.close()
        conn.close()