"""

MÓDULO DE ATUALIZAÇÃO DE AGENDAMENTOS (OPERAÇÃO UPDATE DO CRUD) - BARBEARIA LFJ

RESUMO DE COMO ESTE ARQUIVO FUNCIONA:

1. Consulta Prévia Antes de Alterar:
   - Primeiro, o código pede um ID válido (`ler_id_valido`) e faz um `SELECT`
     para verificar se o agendamento existe no banco `barbearia_lfj`.
   - Se o ID não existir, a função avisa e encerra sem executar `UPDATE`.
   - Se existir, mostra os dados atuais do cliente na tela para dar contexto
     ao barbeiro antes da alteração.

2. Atualização Direcionada por Campo:
   - Em vez de obrigar o usuário a redigir todos os campos novamente, o menu
     permite escolher exatamente o que mudou:
     * Opção 1: Data e horário (`data_horario`).
     * Opção 2: Serviço e valor (`servico` e `valor`, validando preço > 0).
     * Opção 3: Status do atendimento (`status`, ex: Concluído, Cancelado).

3. Cláusula `WHERE id = %s` e Segurança:
   - O filtro `WHERE id = %s` garante que apenas o registro escolhido seja
     modificado — nunca toda a tabela por engano.
   - Os parâmetros `%s` evitam SQL Injection e o `conn.commit()` grava a
     alteração de forma permanente no MySQL Workbench.

4. Tratamento de Erros e Encerramento:
   - O bloco `try / except / finally` captura erros do MySQL e fecha o cursor
     e a conexão ao final da execução.

"""

from mysql.connector import Error
from conexao import conectar
from validacoes import ler_id_valido, ler_texto_obrigatorio, ler_valor_monetario


def atualizar_agendamento():
    """
    Localiza um agendamento pelo ID, exibe os dados atuais e atualiza
    o campo escolhido pelo usuário na tabela 'agendamentos'.
    """
    print("\n--- ATUALIZAR AGENDAMENTO ---")

    # 1. Solicita um ID numérico válido antes de consultar o banco
    id_agendamento = ler_id_valido("Informe o ID do agendamento que deseja alterar: ")

    # 2. Abre a conexão com o MySQL; retorna se não for possível conectar
    conn = conectar()
    if not conn:
        return

    try:
        # dictionary=True permite acessar as colunas pelo nome (ex: registro['cliente_nome'])
        cursor = conn.cursor(dictionary=True)

        # 3. Verifica se o registro existe antes de solicitar novos valores
        cursor.execute("SELECT * FROM agendamentos WHERE id = %s", (id_agendamento,))
        registro = cursor.fetchone()

        if not registro:
            print(f"Nenhum agendamento encontrado com o ID {id_agendamento}.")
            return

        # Exibe o estado atual do agendamento para conferência na tela
        print(
            f"\nRegistro atual: {registro['cliente_nome']} - {registro['servico']} "
            f"({registro['data_horario']}) - Status: {registro['status']}"
        )

        # 4. Submenu para escolher qual parte do agendamento será atualizada
        print("O que deseja atualizar?")
        print("1 - Data e Horário")
        print("2 - Serviço e Valor")
        print("3 - Status (ex: Concluído, Cancelado, Agendado)")
        escolha = input("Opção: ").strip()

        # 5. Executa o comando UPDATE correspondente usando cláusula WHERE no ID
        if escolha == "1":
            nova_data = ler_texto_obrigatorio("Nova data e horário: ")
            cursor.execute(
                "UPDATE agendamentos SET data_horario = %s WHERE id = %s",
                (nova_data, id_agendamento)
            )
        elif escolha == "2":
            novo_servico = ler_texto_obrigatorio("Novo serviço: ")
            novo_valor = ler_valor_monetario("Novo valor (R$): ")
            cursor.execute(
                "UPDATE agendamentos SET servico = %s, valor = %s WHERE id = %s",
                (novo_servico, novo_valor, id_agendamento)
            )
        elif escolha == "3":
            novo_status = ler_texto_obrigatorio("Novo status: ")
            cursor.execute(
                "UPDATE agendamentos SET status = %s WHERE id = %s",
                (novo_status, id_agendamento)
            )
        else:
            print("Opção inválida. Nenhuma alteração realizada.")
            return

        # 6. Confirma e salva permanentemente a modificação no banco de dados
        conn.commit()
        print("Agendamento atualizado com sucesso!")

    except Error as erro:
        # Exibe falhas retornadas pelo MySQL durante a atualização
        print(f"\nErro ao atualizar registro: {erro}")

    finally:
        # 7. Fecha cursor e conexão independentemente de sucesso ou erro
        cursor.close()
        conn.close()