from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base
from app.config.database import db

Base = declarative_base()

class Usuario(Base):
    
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(150))
    email = Column(String(150),unique=True)
    senha = Column(String(150))


    def __init__(self, nome: str, email: str, senha: str):
        self.nome = nome
        self.email = email
        self.senha = senha



    def _nome_vazio(self, nome: str):
        if not nome.strip():
            raise ValueError("O nome não pode ser vazio.")
        return nome

    def _validar_senha(self, senha: str):
        
        if len(senha) < 6:
            raise ValueError("A senha deve ter pelo menos 6 caracteres.")
        return senha
    def _email_vazio(self, email: str):
        if not email.strip():
            raise ValueError("O campo email nao pode ficar vazio.")
        return email


Base.metadata.create_all(bind=db)