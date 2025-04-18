from . import global_bp
from flask_login import current_user, login_required
from flask import render_template, redirect, url_for, request, flash
from app import db
from app.models import users
from werkzeug.security import generate_password_hash

@global_bp.route('/')
@login_required
def root():
    return 'GLOBAL'

@global_bp.route('/usuarios', methods=['POST', 'GET'])
@login_required
def usuarios():
    if current_user.perfil.cargo == 'gestor' or current_user.perfil.cargo == 'gerente':
        if request.method == 'POST':
            # Dados do formulário
            email = request.form['email']
            senha = request.form['senha']
            confirmacao = request.form['confirmar_senha']
            nome = request.form['nome']
            sobrenome = request.form['sobrenome']
            telefone = request.form['telefone']
            setor = request.form['setor']
            cargo = request.form['cargo']

            # Validação simples
            if senha != confirmacao:
                flash('As senhas não coincidem.', 'danger')
                return redirect(url_for('cadastro'))

            # Criação do perfil
            novo_perfil = users.perfil(
                nome=nome,
                sobre_nome=sobrenome,
                tell=telefone,
                setor=setor,
                cargo=cargo
            )
            db.session.add(novo_perfil)
            db.session.flush()  # Garante que o ID seja gerado

            # Criação do usuário
            novo_usuario = users.users(
                email=email,
                pwd=generate_password_hash(senha),
                perfil_id=novo_perfil.id
            )
            db.session.add(novo_usuario)
            db.session.commit()

            flash('Usuário cadastrado com sucesso!', 'success')
            return redirect(url_for('login'))  # ou dashboard

    return render_template('/private/global/cadastro.html')
