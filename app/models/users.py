from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class users(db.Model, UserMixin):

    __tablename__ = 'users'
    id = db.Column('id', db.Integer, primary_key = True, autoincrement=True) 
    email = db.Column('email', db.VARCHAR(100))
    pwd = db.Column('pwd', db.VARCHAR(128))
    falg_alter_pwd = db.Column(db.Boolean, default=False)
    flag_confirm_email = db.Column(db.Boolean, default=False)
    perfil_id = db.Column(db.Integer, db.ForeignKey('perfil.id'), nullable=False)
    
    
class perfil(db.Model):
    __tablename__ = 'perfil'

    id          = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome        = db.Column('nome', db.VARCHAR(15), nullable=False)
    sobre_nome  = db.Column('sobre_nome', db.VARCHAR(100), nullable=False)
    tell        = db.Column('tell', db.VARCHAR(20))
    setor       = db.Column('setor', db.VARCHAR(20))
    cargo       = db.Column('cargo', db.VARCHAR(30), nullable=False)

    usuarios = db.relationship('users', backref='perfil', lazy=True)