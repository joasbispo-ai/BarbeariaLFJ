from mysql.connector import Error
from conexao import conectar
from validacoes import ler_id_valido, ler_texto_obrigatorio

def listar_todos():
    print("\n--- AGENDA COMPLETA | BARBEARIA LFJ ---")
    conn = conectar()
    if not conn:
        return

    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM agendamentos ORDER BY id ASC")
        registros = cursor.fetchall()

        if not registros:
            print("Nenhum agendamento encontrado no sistema.")
            return

        for item in registros:
            print(
                f"ID: {item['id']} | Cliente: {item['cliente_nome']} ({item['telefone']}) | "
                f"Serviço: {item['servico']} | Barbeiro: {item['barbeiro']} | "
                f"Data/Hora: {item['data_horario']} | Valor: R$ {item['valor']:.2f} | "
                f"Status: {item['status']}"
            )
    except Error as erro:
        print(f"\nErro ao consultar agendamentos: {erro}")
    finally:
        cursor.close()
        conn.close()

def consultar_individual():
    print("\n--- BUSCAR AGENDAMENTO ---")
    print("1 - Buscar por ID")
    print("2 - Buscar por nome do cliente")
    opcao = input("Escolha uma opção: ").strip()

    conn = conectar()
    if not conn:
        return

    try:
        cursor = conn.cursor(dictionary=True)
        if opcao == "1":
            id_busca = ler_id_valido("Digite o ID do agendamento: ")
            cursor.execute("SELECT * FROM agendamentos WHERE id = %s", (id_busca,))
        elif opcao == "2":
            nome_busca = ler_texto_obrigatorio("Digite parte do nome do cliente: ")
            cursor.execute("SELECT * FROM agendamentos WHERE cliente_nome LIKE %s", (f"%{nome_busca}%",))
        else:
            print("Opção de busca inválida.")
            return

        resultados = cursor.fetchall()
        if not resultados:
            print("Nenhum registro encontrado para a busca informada.")
            return

        for item in resultados:
            print(
                f"\n[ID {item['id']}] Cliente: {item['cliente_nome']} | Tel: {item['telefone']}\n"
                f"Serviço: {item['servico']} | Barbeiro: {item['barbeiro']}\n"
                f"Data/Hora: {item['data_horario']} | Valor: R$ {item['valor']:.2f} | Status: {item['status']}"
            )
    except Error as erro:
        print(f"\nErro na consulta: {erro}")
    finally:
        cursor.close()
        conn.close()