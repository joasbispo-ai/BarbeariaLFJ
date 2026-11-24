from mysql.connector import Error
from conexao import conectar
from validacoes import ler_texto_obrigatorio, ler_valor_monetario

def cadastrar_agendamento():
    print("\n--- NOVO AGENDAMENTO | BARBEARIA LFJ ---")
    cliente = ler_texto_obrigatorio("Nome do cliente: ")
    telefone = ler_texto_obrigatorio("Telefone/WhatsApp: ")
    servico = ler_texto_obrigatorio("Serviço (ex: Corte Degradê, Barba, Combo): ")
    barbeiro = ler_texto_obrigatorio("Barbeiro responsável: ")
    data_horario = ler_texto_obrigatorio("Data e horário (ex: 25/11/2026 14:30): ")
    valor = ler_valor_monetario("Valor do serviço (R$): ")

    conn = conectar()
    if not conn:
        return "Falha na conexão com o banco de dados."

    try:
        cursor = conn.cursor()
        sql = """
            INSERT INTO agendamentos (cliente_nome, telefone, servico, barbeiro, data_horario, valor)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        dados = (cliente, telefone, servico, barbeiro, data_horario, valor)
        cursor.execute(sql, dados)
        conn.commit()
        return(f"\nAgendamento cadastrado com sucesso! (ID gerado: {cursor.lastrowid})")
    except Error as erro:
        return(f"\nErro ao cadastrar agendamento: {erro}")
    finally:
        if "cursor" in locals():
            cursor.close()
        conn.close()