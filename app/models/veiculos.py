from app import db
from datetime import datetime


class veiculos(db.Model):
    __tablename__ = 'veiculos'

    id      = db.Column('id', db.Integer, primary_key=True)
    placa   = db.Column('placa', db.VARCHAR(10), nullable=False) 
    modelo  = db.Column('modelo', db.VARCHAR(20))
    ano_fab = db.Column('ano_fab', db.VARCHAR(10))
    tipo             = db.Column('tipo', db.VARCHAR(45))
    capacidade_carga = db.Column('capacidade_carga', db.Integer)
    check_lists = db.relationship('Checklist', backref='veiculos', lazy=True, cascade="all, delete-orphan")


    def __init__(self, placa, modelo, capacidade_carga, ano_fab):
        self.codigo_geral_veiculo = f'{placa}{datetime.now().date()}'
        self.placa = placa
        self.modelo = modelo
        self.capacidade_carga = capacidade_carga
        self.ano_fab = ano_fab


class Checklist(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    codigo = db.Column(db.String(20), unique=True, nullable=False)
    veiculo_id = db.Column(db.Integer, db.ForeignKey('veiculos.id'), nullable=False)
    data_check = db.Column(db.DateTime, default=db.func.current_timestamp())
    user = db.Column('user', db.ForeignKey('users.id'), nullable=False)
    
    usuario = db.relationship('users', backref='checklists')
    itens = db.relationship('ChecklistItem', backref='checklist', lazy=True, cascade="all, delete-orphan")
    
    def to_dict(self):
        return {"id": self.id, "codigo": self.codigo}


# ✅ Tabela de Itens do Checklist (Atributos Variáveis)
class ChecklistItem(db.Model):  
    id = db.Column(db.Integer, primary_key=True)
    checklist_id = db.Column(db.Integer, db.ForeignKey('checklist.id'), nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    valor = db.Column(db.String(255))  # Pode armazenar texto, números ou status