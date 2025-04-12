# app/blueprints/auth/__init__.py
# Aqui eu crio o blueprint de autenticação (auth_bp) e importo as rotas

from flask import Blueprint

# Criação do blueprint de autenticação
auth_bp = Blueprint("auth", __name__, template_folder="templates")

# Importa as rotas (para registrar elas no blueprint)
from . import routes