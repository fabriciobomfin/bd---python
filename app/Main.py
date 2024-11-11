import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.repositories.usuario_repository import UsuarioRepository
from app.services.usuario_service import UsuarioService
from config.database import Session

def solicitar_dados_usuario(atualizando=False):
    nome = input("Digite o nome do usuário: ") if not atualizando else input("Digite o novo nome (ou pressione Enter para manter): ")
    email = input("Digite o e-mail do usuário: ") if not atualizando else None
    senha = input("Digite a senha do usuário: ") if not atualizando else input("Digite a nova senha (ou pressione Enter para manter): ")
    return nome, email, senha

def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)

    opcoes = {
        "1": "Adicionar usuário",
        "2": "Pesquisar um usuário",
        "3": "Atualizar dados de um usuário",
        "4": "Excluir um usuário",
        "5": "Exibir todos os usuários cadastrados",
        "0": "Sair"
    }

    while True:
        print("\n=== SENAI SOLUTION ===")
        for key, value in opcoes.items():
            print(f"{key} - {value}")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            nome, email, senha = solicitar_dados_usuario()
            try:
                service.criar_usuario(nome=nome, email=email, senha=senha)
            except Exception as e:
                print(f"Erro ao adicionar usuário: {e}")

        elif opcao == "2":
            email = input("Digite o e-mail do usuário que deseja pesquisar: ")
            try:
                usuario = repository.pesquisar_usuario(email)
                if usuario:
                    print(f"Usuário encontrado - Nome: {usuario.nome} - Email: {usuario.email}")
                else:
                    print("Usuário não encontrado.")
            except Exception as e:
                print(f"Erro ao pesquisar usuário: {e}")

        elif opcao == "3":
            email = input("Digite o e-mail do usuário que deseja atualizar: ")
            usuario = repository.pesquisar_usuario(email)
            if usuario:
                nome, _, senha = solicitar_dados_usuario(atualizando=True)
                usuario.nome = nome if nome else usuario.nome
                usuario.senha = senha if senha else usuario.senha
                try:
                    repository.salvar_usuario(usuario)
                    print("Dados do usuário atualizados com sucesso!")
                except Exception as e:
                    print(f"Erro ao atualizar usuário: {e}")
            else:
                print("Usuário não encontrado.")

        elif opcao == "4":
            email = input("Digite o e-mail do usuário que deseja excluir: ")
            try:
                usuario = repository.pesquisar_usuario(email)
                if usuario:
                    repository.excluir_usuario(usuario)
                    print("Usuário excluído com sucesso!")
                else:
                    print("Usuário não encontrado.")
            except Exception as e:
                print(f"Erro ao excluir usuário: {e}")

        elif opcao == "5":
            try:
                usuarios = repository.listar_todos_usuarios()
                if usuarios:
                    print("\nLista de usuários cadastrados:")
                    for usuario in usuarios:
                        print(f"Nome: {usuario.nome} - Email: {usuario.email}")
                else:
                    print("Nenhum usuário cadastrado.")
            except Exception as e:
                print(f"Erro ao listar usuários: {e}")

        elif opcao == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    os.system("cls || clear")
    main()
