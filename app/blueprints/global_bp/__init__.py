from flask import Blueprint

global_bp = Blueprint('global', __name__, template_folder='templates')
from . import routes