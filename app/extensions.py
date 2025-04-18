from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager 
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = '/login'  # Página de login quando o usuário não estiver autenticado
login_manager.login_message = 'Por favor, faça login para acessar esta página.'