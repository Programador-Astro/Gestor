# app/blueprints/auth/routes.py
# Aqui eu defino as rotas de autenticação (login, logout, etc)

from flask_login import login_user, logout_user, current_user
from flask import render_template, request, redirect, url_for, flash
from . import auth_bp
from ...config import testar_conexao
from ...extensions import db
from app.models import users

# Rota de login
@auth_bp.route("/login", methods=["POST"])
def login():
    logout_user(    )

    #Capturando os DADOS
    email = request.form.get('email')
    pwd = request.form.get('pwd')

    #Verificando os DADOS
    user = users.users.query.filter_by(email=email).first()
    try:
        if user:
            if user.pwd == pwd:
                login_user(user)
                return f'{user} LOGADO'
        else:
            flash('Usuario ou senha Invalido')
            return redirect(url_for('index'))
    except:
        return redirect(url_for('index'))
    flash('Usuario ou senha invalido')
    return redirect(url_for('index'))
     



# Rota de logout (simples por enquanto)
@auth_bp.route("/logout")
def logout():
    flash("Deslogado.", "info")
    logout_user()