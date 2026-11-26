"""
Módulo de consulta de agendamentos (operação READ do CRUD).
Suporta listagem geral da agenda e busca filtrada por ID ou nome do cliente.
"""

from mysql.connector import Error
from conexao import conectar
from validacoes import ler_id_valido, ler_texto_obrigatorio


def listar_todos():
    """
    Consulta e exibe todos os agendamentos cadastrados, ordenados por ID.
    """
    print("\n--- AGENDA COMPLETA | BARBEARIA LFJ ---")
    conn = conectar()
    if not conn:
        return

    try:
        # dictionary=True faz cada linha virar um dicionário acessível pelo nome da coluna
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM agendamentos ORDER BY id ASC")
        registros = cursor.fetchall()

        if not registros:
            print("Nenhum agendamento encontrado no sistema.")
            return

        # Formata e imprime cada agendamento em uma linha legível no terminal
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
    """
    Permite localizar um ou mais agendamentos específicos por ID exato
    ou por trecho do nome do cliente (busca parcial com LIKE).
    """
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
            # Os curingas % permitem encontrar nomes que contenham o termo digitado
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