from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

#Parâmetros de conexãob para BD MySQL.

db_user = "user"
db_password = "user_password"

#localhost = minha maquinha
db_host = "localhost"
db_port = "3306"
db_name = "meu_banco"


# URL de conexão para BD(Banco de Dados) MySQL.
#DARABASE_URL = f"mysql+pymysql://usuario:senha@host:porta/nome_bd"
DATABASE_URL = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"


# Connectando ao banco de dados.
db = create_engine(DATABASE_URL)
Session = sessionmaker(bind=db)
session = Session()

@contextmanager
def get_db():
    bd = Session()# Cria uma sessão para açôes no banco de dados.
    try:
        yield bd # Caso a sessão realize todas as tarefas, salva a operação.
        db.comit()
    except Exception as erro:
        db.rollback() # Desfaz todas alterações em caso de erro em alguma operação.
        raise erro #Lança ema exceçâo.
    finally:
        db.close() # Fecha sessão 