import mysql.connector
import os

def conectar():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",          
            password="root",      
            database="agro_db"    
        )
    except mysql.connector.Error as err:
        print(f"Erro de Conexão: {err}")
        return None

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    input('\nPressione Enter para voltar ao menu...')
