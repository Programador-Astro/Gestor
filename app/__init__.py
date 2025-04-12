# app/__init__.py
# Aqui eu configuro e inicializo minha aplicação Flask, extensões e blueprints

from flask import Flask, render_template, redirect, url_for, request
from .extensions import db, migrate
from .models import users  # Importação dos models para o Flask-Migrate reconhecer
from .blueprints import register_blueprints


def creat_app():
    
    app = Flask(__name__)
    
    #Carregando as config do projeto
    app.config.from_object("app.config.Config")

    #Inicializando as extensões
    db.init_app(app)
    migrate.init_app(app, db)

    #Registra o blue print da aplicação
    register_blueprints(app)

    #home page
    @app.route('/', methods=['GET'])
    def home():
      
        email = request.form.get('email')
        pwd = request.form.get('pwd')
        
        return render_template('login.html')



    return app