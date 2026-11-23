from mysql.connector import Error
from conexao import conectar
from validacoes import ler_id_valido

def excluir_agendamento():
    print("\n--- EXCLUIR AGENDAMENTO ---")
    id_agendamento = ler_id_valido("Informe o ID do agendamento que deseja excluir: ")

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

        print(f"\nAgendamento localizado: {registro['cliente_nome']} | {registro['servico']} | {registro['data_horario']}")
        confirmacao = input("Tem certeza que deseja excluir este registro? (S/N): ").strip().upper()

        if confirmacao == "S":
            cursor.execute("DELETE FROM agendamentos WHERE id = %s", (id_agendamento,))
            conn.commit()
            print("Agendamento excluído permanentemente.")
        else:
            print("Operação cancelada pelo usuário.")
    except Error as erro:
        print(f"\nErro ao excluir registro: {erro}")
    finally:
        cursor.close()
        conn.close()