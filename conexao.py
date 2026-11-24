import mysql.connector
from mysql.connector import Error

def conectar():
    """Estabelece e retorna a conexão com o banco barbearia_lfj."""
    try:
        conexao = mysql.connector.connect(
            host="127.0.0.1",
            port=3308,          # Porta exata exibida no seu XAMPP
            user="root",
            password="",
            database="barbearia_lfj",
            use_pure=True
        )
        return conexao
    except Error as erro:
        print(f"\n[ERRO DE CONEXÃO] Não foi possível conectar ao MySQL: {erro}")
        return None