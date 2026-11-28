"""

MÓDULO DE CADASTRO DE AGENDAMENTOS (OPERAÇÃO CREATE DO CRUD) - BARBEARIA LFJ

RESUMO DE COMO ESTE ARQUIVO FUNCIONA:

1. Coleta e Validação de Dados (RF01 + RF06):
   - Antes de abrir conexão com o banco, o código solicita todos os campos do
     agendamento usando as funções de `validacoes.py`. Isso impede o envio de
     textos vazios ou valores negativos/inválidos para o MySQL.

2. Inserção Segura com Consultas Parametrizadas (%s):
   - Os valores digitados pelo barbeiro são passados em uma tupla (`dados`)
     separada da string SQL. O conector do MySQL trata os tipos automaticamente
     e protege o sistema contra falhas de SQL Injection.

3. Persistência com `conn.commit()` e Retorno do ID:
   - Como o comando `INSERT` altera o estado do banco, o `conn.commit()` é
     obrigatório para gravar o registro definitivamente no MySQL Workbench.
   - Utilizamos `cursor.lastrowid` para informar ao usuário o número exato do
     ID gerado automaticamente pelo `AUTO_INCREMENT` do banco.

4. Encerramento Seguro da Conexão:
   - O bloco `try / except / finally` garante que qualquer erro de banco seja
     tratado sem quebrar o programa e que o cursor e a conexão sejam fechados
     ao final da operação.

"""

from mysql.connector import Error
from conexao import conectar
from validacoes import ler_texto_obrigatorio, ler_valor_monetario, ler_texto_ou_voltar


def cadastrar_agendamento():
    """
    Solicita os dados do atendimento ao usuário, valida as entradas e insere
    um novo registro na tabela 'agendamentos' do banco 'barbearia_lfj'.
    """
    print("\n--- NOVO AGENDAMENTO | BARBEARIA LFJ ---")
    
    cliente = ler_texto_ou_voltar("Nome do cliente (0 para voltar): ")  # Lê o nome do cliente permitindo digitar 0 para voltar
    if cliente is None:  # Verifica se o usuário escolheu voltar
        print("Cadastro cancelado. Voltando ao menu principal...")  # Informa que o cadastro foi cancelado
        
        return  # Encerra a função e retorna ao menu principal

    # 1. Coleta e validação das entradas (evita campos em branco ou preços inválidos)
    telefone = ler_texto_obrigatorio("Telefone/WhatsApp: ")
    servico = ler_texto_obrigatorio("Serviço (ex: Corte Degradê, Barba, Combo): ")
    barbeiro = ler_texto_obrigatorio("Barbeiro responsável: ")
    data_horario = ler_texto_obrigatorio("Data e horário (ex: 26/11/2026 14:30): ")
    valor = ler_valor_monetario("Valor do serviço (R$): ")

    # 2. Abre a conexão com o banco de dados MySQL
    conn = conectar()
    if not conn:
        # Encerra a função caso a conexão tenha falhado (o erro já foi exibido em conexao.py)
        return

    try:
        # Cria o cursor responsável por executar comandos SQL no banco
        cursor = conn.cursor()

        # 3. Prepara o comando SQL de inserção (a coluna 'status' recebe 'Agendado' por padrão no banco)
        sql = """
            INSERT INTO agendamentos (cliente_nome, telefone, servico, barbeiro, data_horario, valor)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        # Tupla contendo os valores na mesma ordem dos marcadores %s acima
        dados = (cliente, telefone, servico, barbeiro, data_horario, valor)

        # Executa o INSERT no servidor MySQL
        cursor.execute(sql, dados)

        # Confirma a transação para salvar os dados permanentemente no MySQL Workbench
        conn.commit()

        # Exibe confirmação junto com o ID gerado automaticamente pelo banco
        return(f"\nAgendamento cadastrado com sucesso! (ID gerado: {cursor.lastrowid})")

    except Error as erro:
        # Captura e exibe eventuais falhas de execução no banco de dados
        return (f"\nErro ao cadastrar agendamento: {erro}")

    finally:
        # 4. Fecha o cursor e a conexão para liberar recursos do servidor
        if "cursor" in locals():cursor.close()
        conn.close()