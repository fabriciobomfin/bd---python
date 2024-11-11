import pytest
from app.models.usuario_model import Usuario
from app.repositories.usuario_repository import UsuarioRepository
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

@pytest.fixture 
def session():
    engine = create_engine("sqlite:///:memory:") 
    Session = sessionmaker(bind=engine)
    session = Session()
    Usuario.metadata.create_all(engine)
    yield session
    session.close()

@pytest.fixture
def usuario_repository(session):
    return UsuarioRepository(session)

@pytest.fixture
def usuario_exemplo():
    return Usuario(nome="Exemplo", email="exemplo@example.com")

def test_salvar_e_pesquisar_usuario(usuario_repository, usuario_exemplo):
    usuario_repository.salvar_usuario(usuario_exemplo)
    usuario = usuario_repository.pesquisar_usuario("exemplo@example.com")
    assert usuario is not None
    assert usuario.email == "exemplo@example.com"

def test_excluir_usuario(usuario_repository, usuario_exemplo):
    usuario_repository.salvar_usuario(usuario_exemplo)
    usuario_repository.excluir_usuario(usuario_exemplo)
    assert usuario_repository.pesquisar_usuario("exemplo@example.com") is None

def test_listar_todos_usuario(usuario_repository, usuario_exemplo):
    usuario_repository.salvar_usuario(usuario_exemplo)
    assert len(usuario_repository.listar_todos_usuario()) == 1


