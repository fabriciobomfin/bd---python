from app.models.usuario_model import Usuario
from app.repositories.usuario_repository import UsuarioRepository

class UsuarioService:
    def __init__(self, repository: UsuarioRepository ) -> None:
          self.repository = repository
        
    def criar_usuario(self, nome: str, email: str, senha: str):
        try:
              usuario = Usuario(nome=nome, email=email, senha=senha)
              
              novo_usuario = self.repository.pesquisar_usuario(usuario.email)

              if novo_usuario:
                print("Usuário já cadastrrado no banco de dados. ")
                return
        
              self.repository.salvar_usuario(usuario)
              print("Usuário cadastrado com sucesso!")
        except TypeError as erro:
                print(f"Erro ao cadastrar usuário: {erro}")
        except Exception as erro:
                print(f"Ocorreu um erro inesperado: {erro}")

    def listar_todos_usuarios(self):
         return self.repository.listar_suario()
              