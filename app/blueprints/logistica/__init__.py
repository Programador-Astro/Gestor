from flask import Blueprint

logistica_bp = Blueprint('logistica', __name__, template_folder='templates')
from . import routes