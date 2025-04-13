from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class users(db.Model):
    __tablename__ = 'users'
    id = db.Column('id', db.Integer, primary_key = True)
    email = db.Column('email', db.VARCHAR(100))
    pwd = db.Column('pwd', db.VARCHAR(128))
    falg_alter_pwd = db.Column(db.Boolean, default=False)
    flag_confirm_email = db.Column(db.Boolean, default=False)
    perfil_id = db.Column(db.Integer, db.ForeignKey('perfil.id'), nullable=False)
    
    def set_pwd(self, pwd):
        self.pwd = generate_password_hash(pwd)

    def verify_pwd(self, pwd):
        return check_password_hash(self.pwd, pwd)
    
    def __repr__(self):
        return f'<User {self.email}>'

    # Métodos requeridos pelo Flask-Login:
    
    def is_authenticated(self):
        return True  # Retorne True se o usuário estiver autenticado

    def is_active(self):
        # Normalmente, você verifica aqui se a conta do usuário está ativa
        return True  # Retorne True se a conta do usuário estiver ativa

    def is_anonymous(self):
        return False  # Retorne True se o usuário for anônimo, senão False

    def get_id(self):
        return str(self.id)  # Retorna o ID do usuário como string
class perfil(db.Model):
    __tablename__ = 'perfil'

    id          = db.Column(db.Integer, primary_key=True)
    nome        = db.Column('nome', db.VARCHAR(15), nullable=False)
    sobre_nome  = db.Column('sobre_nome', db.VARCHAR(100), nullable=False)
    tell        = db.Column('tell', db.VARCHAR(20))
    cargo       = db.Column('cargo', db.VARCHAR(30), nullable=False)

    usuarios = db.relationship('users', backref='perfil', lazy=True)