import pytest
from app.models.usuario_model import Usuario

def test_nome_vazio():
    with pytest.raises(ValueError, match="O nome não pode ser vazio."):
        Usuario(nome="", email="test@teste.com", senha="senha123")

def test_email_vazio():
    with pytest.raises(ValueError, match="O campo email nao pode ficar vazio."):
        Usuario(nome="Teste", email="", senha="senha123")

def test_senha_vazia():
    with pytest.raises(ValueError, match="A senha não pode ser vazia."):
        Usuario(nome="Teste", email="test@teste.com", senha="")

def test_tipo_nome_invalido():
    with pytest.raises(TypeError, match="Nome inválido."):
        Usuario(nome=123, email="test@teste.com", senha="senha123")

def test_tipo_email_invalido():
    with pytest.raises(TypeError, match="Email inválido."):
        Usuario(nome="Teste", email=123, senha="senha123")

def test_tipo_senha_invalida():
    with pytest.raises(TypeError, match="Senha inválida."):
        Usuario(nome="Teste", email="test@teste.com", senha=123)
