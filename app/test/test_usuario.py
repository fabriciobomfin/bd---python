import pytest
from app.models.usuario_model import Usuario

@pytest.fixture
def usuario_valido():
    return Usuario("Marta", "marta1@gmail.com", "senha123")

# Testes de dados válidos
def test_usuario_valido(usuario_valido):
    assert usuario_valido.nome == "Marta"
    assert usuario_valido.email == "marta1@gmail.com"
    assert usuario_valido.senha == "senha123"

# Testes de exceções
def test_nome_vazio():
    with pytest.raises(ValueError, match="O nome não pode ser vazio."):
        Usuario("", "email@gmail.com", "senha123")

def test_email_vazio():
    with pytest.raises(ValueError, match="O campo email nao pode ficar vazio."):
        Usuario("Nome", "", "senha123")

def test_senha_vazia():
    with pytest.raises(ValueError, match="A senha não pode ser vazia."):
        Usuario("Nome", "email@gmail.com", "")

def test_tipo_nome_invalido():
    with pytest.raises(TypeError, match="Nome inválido."):
        Usuario(123, "email@gmail.com", "senha123")

def test_tipo_email_invalido():
    with pytest.raises(TypeError, match="Email inválido."):
        Usuario("Nome", 12345, "senha123")

def test_tipo_senha_invalida():
    with pytest.raises(TypeError, match="Senha inválida."):
        Usuario("Nome", "email@gmail.com", 12345)
