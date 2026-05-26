import mysql.connector
import os

def conectar():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",          # Usuário padrão do MySQL
            password="root",      # Coloque aqui a senha do SEU MySQL (se não tiver senha, deixe vazio "")
            database="agro_db"    # Conecta direto no banco que você já criou
        )
    except mysql.connector.Error as err:
        print(f"Erro de Conexão: {err}")
        return None

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    input('\nPressione Enter para voltar ao menu...')