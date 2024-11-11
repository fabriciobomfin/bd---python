from app.models.usuario_model import Usuario
from app.repositories.usuario_repository import UsuarioRepository

class UsuarioService:
    def __init__(self, repository: UsuarioRepository) -> None:
        self.repository = repository

    def criar_usuario(self, nome: str, email: str, senha: str):
        try:
            usuario = Usuario(nome=nome, email=email, senha=senha)
            if self.repository.pesquisar_usuario(email):
                print("Usuário já cadastrado no banco de dados.")
                return
            self.repository.salvar_usuario(usuario)
            print("Usuário cadastrado com sucesso!")
        except Exception as erro:
            print(f"Erro ao cadastrar usuário: {erro}")

    def listar_todos_usuarios(self):
        return self.repository.listar_todos_usuarios()
