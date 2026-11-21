import mysql.connector
from mysql.connector import Error

def conectar():
    """Estabelece e retorna a conexão com o banco barbearia_lfj."""
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",          # Altere se o seu usuário no Workbench for outro
            password="SUA_SENHA", # Coloque a senha do seu MySQL Workbench
            database="barbearia_lfj"
        )
        return conexao
    except Error as erro:
        print(f"\n[ERRO DE CONEXÃO] Não foi possível conectar ao MySQL: {erro}")
        return None