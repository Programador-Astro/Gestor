# app/config.py
# Configurações gerais da aplicação. Depois eu posso separar por ambiente (dev, prod, etc)

import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "mysql+pymysql://usuario:senha@localhost/meubanco")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY", "minha_chave_secreta")