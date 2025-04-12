# app/blueprints/auth/routes.py
# Aqui eu defino as rotas de autenticação (login, logout, etc)

from flask import render_template, request, redirect, url_for, flash
from . import auth_bp

# Rota de login
@auth_bp.route("/login", methods=["POST"])
def login():
    #Capturando os DADOS
    email = request.form.get('email')
    pwd = request.form.get('pwd')
    

    #Consultando e Validando os dados
    

# Rota de logout (simples por enquanto)
@auth_bp.route("/logout")
def logout():
    flash("Usuário deslogado.", "info")
    return redirect(url_for("auth.login"))