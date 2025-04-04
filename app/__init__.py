from flask import Flask, request, render_template
from flask_login import LoginManager
from sqlalchemy import text
from dotenv import load_dotenv
import os
import pandas as pd
from app.db import db
from app.models.estoque_model import *

app = Flask(__name__)
lm = LoginManager(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
load_dotenv()

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL') 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



#Informando o flask qual é minha pasta padrão para upload de arquivos
UPLOAD_FOLDER = 'uploads'
UPLOAD_FOLDER_FINANCEIRO = 'uploads/financeiro'
ALLOWED_EXTENCIONS = ['csv']
app.config['UPLOAD_FOLDER_FINANCEIRO'] = UPLOAD_FOLDER_FINANCEIRO
#criando pasta caso não exista
os.makedirs(UPLOAD_FOLDER_FINANCEIRO, exist_ok=True)
os.makedirs(UPLOAD_FOLDER, exist_ok=True)



#Criação de esquemas (USADO APENAS PARA OTIMIZAR OS DEBUGS)
def criar_schema(nome_schema):
    with app.app_context():
        db.session.execute(text(f"CREATE SCHEMA IF NOT EXISTS {nome_schema};"))
        db.session.commit()


#(USADO APENAS PARA OTIMIZAR OS DEBUGS)
def start_padrao():
    categorias = Nome_Categoria.query.all()
    nomes = Nome_Produto.query.all()
    #Verificando se as categorias são existentes
    if len(categorias) <=0 and len(nomes) <=0:
        #Criando as categorias
        lista_categorias = ['Frutas', 'Embalagens', 'Rotulos']
        for categoria in lista_categorias:
            nova_categoria = Nome_Categoria(categoria)
            db.session.add(nova_categoria)
        #Criando os nomes
        lista_nomes = ['Morango', 'Banana', 'CX Natureza', 'CX Doce Gelato']
        for nome in lista_nomes:
            novo_nome = Nome_Produto(nome)
            db.session.add(novo_nome)
        db.session.commit()
    return
    


with app.app_context():
    criar_schema('estoque_producao')
    db.create_all()
    start_padrao()
