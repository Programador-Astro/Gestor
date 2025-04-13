# app/__init__.py
# Aqui eu configuro e inicializo minha aplicação Flask, extensões e blueprints

from flask import Flask, render_template, redirect, url_for, request, session
from flask_login import current_user, logout_user

from .extensions import db, migrate, login_manager
from .models import users  # Importação dos models para o Flask-Migrate reconhecer
from .blueprints import register_blueprints


def creat_app():
    app = Flask(__name__)
    #Carregando as config do projeto
    app.config.from_object("app.config.Config")

    @login_manager.user_loader
    def load_user(user_id):
        return users.users.query.get(int(user_id))

    #Inicializando as extensões
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
            db.create_all()  # Criando as atabelas

    #Registra o blue print da aplicação
    register_blueprints(app)


    #Verificando se está logado na rota raiz e redirecionando
    @app.route('/')
    def index():
        if current_user.is_authenticated:
            return redirect(url_for('{current_user.setor}.home'))
        else: 
            return redirect(url_for('login'))
    #login page
    @app.route('/login', methods=['GET'])
    def login():
        logout_user()
        return render_template('login.html')
    #Rota de cadastro
    @app.route('/cadastrar')
    def cadastrar():
        logout_user()
        return render_template('cadastrar.html')
    



    return app