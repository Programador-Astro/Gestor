# app/config.py
# Configurações gerais da aplicação. Depois eu posso separar por ambiente (dev, prod, etc)
from dotenv import load_dotenv
import os
load_dotenv()
class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY")
    

from app import db
from sqlalchemy.exc import OperationalError

def testar_conexao():
    try:
        # Executa uma query simples só pra verificar
        db.session.execute("SELECT 1")
        print("✅ Conexão com o banco de dados bem-sucedida!")
    except OperationalError as e:
        print("❌ Falha ao conectar com o banco de dados:")
        print(e)