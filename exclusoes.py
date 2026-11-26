"""

MÓDULO DE EXCLUSÃO DE AGENDAMENTOS (OPERAÇÃO DELETE DO CRUD) - BARBEARIA LFJ

RESUMO DE COMO ESTE ARQUIVO FUNCIONA:

1. Localização e Conferência do Registro:
   - O código pede um ID numérico válido (`ler_id_valido`) e busca o registro
     correspondente na tabela `agendamentos` do banco `barbearia_lfj`.
   - Se o ID não existir, informa ao usuário e encerra sem apagar nada.
   - Se existir, exibe os dados do agendamento na tela para que o barbeiro
     confirme qual atendimento está prestes a remover.

2. Confirmação Explícita Antes de Apagar (Segurança Operacional):
   - A exclusão no banco é permanente. Por isso, o sistema exige que o
     usuário digite `S` (maiúsculo ou minúsculo) para confirmar.
   - Qualquer outra resposta cancela a operação com segurança, preservando o
     registro intacto no MySQL Workbench.

3. Cláusula `WHERE id = %s` e `conn.commit()`:
   - O `WHERE id = %s` garante que apenas o registro selecionado seja excluído.
   - O uso de `%s` protege contra SQL Injection, e o `conn.commit()` efetiva
     a remoção no banco de dados.

4. Tratamento de Erros e Encerramento Seguro:
   - O bloco `try / except / finally` captura falhas do MySQL e fecha o cursor
     e a conexão ao final da execução.

"""

from mysql.connector import Error
from conexao import conectar
from validacoes import ler_id_valido


def excluir_agendamento():
    """
    Localiza um agendamento pelo ID, exibe os detalhes para conferência
    e remove o registro da tabela 'agendamentos' somente após confirmação.
    """
    print("\n--- EXCLUIR AGENDAMENTO ---")

    # 1. Solicita um ID inteiro positivo antes de consultar o banco
    id_agendamento = ler_id_valido("Informe o ID do agendamento que deseja excluir: ")

    # 2. Abre a conexão com o MySQL; retorna se houver falha na conexão
    conn = conectar()
    if not conn:
        return

    try:
        # dictionary=True permite acessar as colunas do registro pelo nome
        cursor = conn.cursor(dictionary=True)

        # 3. Consulta o agendamento para verificar se existe e mostrar seus dados
        cursor.execute("SELECT * FROM agendamentos WHERE id = %s", (id_agendamento,))
        registro = cursor.fetchone()

        if not registro:
            print(f"Nenhum agendamento encontrado com o ID {id_agendamento}.")
            return

        # Exibe os dados encontrados para evitar exclusão por engano
        print(
            f"\nAgendamento localizado: {registro['cliente_nome']} | "
            f"{registro['servico']} | {registro['data_horario']}"
        )

        # 4. Solicita confirmação explícita ('S' para confirmar, qualquer outra tecla cancela)
        confirmacao = input("Tem certeza que deseja excluir este registro? (S/N): ").strip().upper()

        if confirmacao == "S":
            # Executa a exclusão filtrando apenas pelo ID informado
            cursor.execute("DELETE FROM agendamentos WHERE id = %s", (id_agendamento,))

            # Confirma e salva permanentemente a exclusão no MySQL Workbench
            conn.commit()
            print("Agendamento excluído permanentemente.")
        else:
            # Cancela a operação sem alterar o banco de dados
            print("Operação cancelada pelo usuário.")

    except Error as erro:
        # Exibe falhas retornadas pelo MySQL durante a exclusão
        print(f"\nErro ao excluir registro: {erro}")

    finally:
        # 5. Fecha cursor e conexão independentemente de sucesso ou erro
        cursor.close()
        conn.close()