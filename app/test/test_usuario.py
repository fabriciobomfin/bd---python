import pytest
from app.models.usuario_model import Usuario

# Teste: Nome vazio retorna mensagem de erro
def test_usuario_nome_vazio_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="O que está sendo solicitado está vazio."):
        Usuario("", "marta@gmail.com", "1234")

# Teste: Nome inválido (número) retorna mensagem de erro
def test_usuario_nome_invalido_erro():
    with pytest.raises(TypeError, match="O que está sendo solicitado está inválido."):
        Usuario(000, "marta@gmail.com", "1234")

# Teste: Email vazio retorna mensagem de erro
def test_usuario_email_vazio_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="O que está sendo solicitado está vazio."):
        Usuario("Marta", "", "1234")

# Teste: Email inválido (número) retorna mensagem de erro
def test_usuario_email_invalido_erro():
    with pytest.raises(TypeError, match="O que está sendo solicitado está inválido."):
        Usuario("Marta", 000, "1234")

# Teste: Senha vazia retorna mensagem de erro
def test_usuario_senha_vazio_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="O que está sendo solicitado está vazio."):
        Usuario("Marta", "marta@gmail.com", "")

# Teste: Senha inválida (número) retorna mensagem de erro
def test_usuario_senha_invalido_erro():
    with pytest.raises(TypeError, match="O que está sendo solicitado está inválido."):
        Usuario("Marta", "marta@gmail.com", 1234)
