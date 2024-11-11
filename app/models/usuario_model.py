from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    senha = Column(String, nullable=False)

    def __init__(self, nome, email, senha):
        # Validando os dados antes de atribuir aos atributos
        self.nome = self._validar_nome(nome)
        self.email = self._validar_email(email)
        self.senha = self._validar_senha(senha)

    def _validar_nome(self, nome):
        if not nome:
            raise ValueError("O nome não pode ser vazio.")
        if not isinstance(nome, str):
            raise TypeError("Nome inválido.")
        return nome

    def _validar_email(self, email):
        if not email:
            raise ValueError("O campo email nao pode ficar vazio.")
        if not isinstance(email, str):
            raise TypeError("Email inválido.")
        return email

    def _validar_senha(self, senha):
        if not senha:
            raise ValueError("A senha não pode ser vazia.")
        if not isinstance(senha, str):
            raise TypeError("Senha inválida.")
        if len(senha) < 6:
            raise ValueError("A senha deve ter pelo menos 6 caracteres.")
        return senha
