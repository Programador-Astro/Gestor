
from flask import render_template, redirect, url_for, request, session
from app import app
from sqlalchemy import text

from datetime import datetime
from app.models.models import User
from app.db import db

import os


#Imports para o register dos Blue Prints
from app.routes.auth import auth_bp
from app.routes.gerencia import gerencia_bp
from app.routes.estoque import estoque_bp
from app.routes.logistica import logistica_bp
from app.routes.financeiro import financeiro_bp


#Viwe raiz
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    
    if request.method == 'POST':
        user = request.form.get('user')
        pwd = request.form.get('pwd')
 
        return redirect(url_for('auth.root',user=user ,pwd=pwd))



#Register Blue Prints
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(gerencia_bp, url_prefix='/gerencia')
app.register_blueprint(estoque_bp, url_prefix='/estoque')
app.register_blueprint(logistica_bp, url_prefix='/logistica')
app.register_blueprint(financeiro_bp, url_prefix ='/financeiro')


if __name__ == "__main__":
    from threading import Thread
    def run():
        app.run()
    thread = Thread(target=run)
    thread.start()
    
