"""

MÓDULO DE CONEXÃO COM O BANCO DE DADOS (MYSQL / WORKBENCH) - BARBEARIA LFJ

RESUMO DE COMO ESTE ARQUIVO FUNCIONA:

1. Ponte entre Python e MySQL:
   - Este módulo centraliza a abertura da conexão com o banco `barbearia_lfj`
     usando a biblioteca oficial `mysql-connector-python`.
   - Assim, os outros arquivos (`cadastro.py`, `consultas.py`, `atualizacoes.py`
     e `exclusoes.py`) não precisam repetir configurações de acesso ao banco;
     basta importar e chamar a função `conectar()`.

2. Parâmetros de Conexão:
   - `host="localhost"`: Indica que o servidor MySQL está rodando na própria
     máquina onde o código está sendo executado.
   - `user` e `password`: Credenciais do usuário no MySQL Workbench. Cada membro
     da equipe deve conferir ou ajustar a senha local ao rodar o projeto.
   - `database="barbearia_lfj"`: Seleciona diretamente o banco criado no script
     `banco_barbearia.sql`.

3. Tratamento Seguro de Falhas (`try / except`):
   - Se o serviço do MySQL estiver parado, o banco ainda não tiver sido criado
     ou a senha estiver incorreta, o `mysql.connector` lança um erro (`Error`).
   - Em vez de o programa travar com um traceback confuso, o `except` exibe uma
     mensagem clara e retorna `None` para que a função chamadora pare com segurança.

"""

import mysql.connector
from mysql.connector import Error

def conectar():
    """Estabelece e retorna a conexão com o banco barbearia_lfj."""
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",          
            password="barbearia123", 
            database="barbearia_lfj"
        )
        return conexao
    # Exibe o motivo exato da falha (ex: acesso negado, servidor offline ou banco inexistente)
    except Error as erro:
        print(f"\n[ERRO DE CONEXÃO] Não foi possível conectar ao MySQL: {erro}")
        return None