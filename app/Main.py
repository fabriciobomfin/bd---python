import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),' .. ')))
from app.repositories.usuario_repository import UsuarioRepository
from app.services.usuario_service import UsuarioService

from config.database import Session

def main():
    # Inicialização da sessão e das instâncias de repositório e serviço
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)

    while True:
        # Menu de opções
        print("\nEscolha uma opção:")
        print("1 - Adicionar usuário")
        print("2 - Pesquisar um usuário")
        print("3 - Atualizar dados de um usuário")
        print("4 - Excluir um usuário")
        print("5 - Exibir todos os usuários")
        print("0 - Sair")

        opcao = input("Digite o número da opção desejada: ")
        
        if opcao == "1":
            
            nome = input("Digite o nome do usuário: ")
            email = input("Digite o e-mail do usuário: ")
            senha = input("Digite a senha do usuário: ")
            service.criar_usuario(nome=nome, email=email, senha=senha)
        
        elif opcao == "2":
            
            email = input("Digite o e-mail do usuário que deseja pesquisar: ")
            usuario = repository.pesquisar_usuario(email)
            if usuario:
                print(f"Usuário encontrado - Nome: {usuario.nome} - Email: {usuario.email} - Senha: {usuario.senha}")
            else:
                print("Usuário não encontrado.")
        
        elif opcao == "3":
            
            email = input("Digite o e-mail do usuário que deseja atualizar: ")
            usuario = repository.pesquisar_usuario(email)
            if usuario:
                novo_nome = input("Digite o novo nome (ou pressione Enter para manter o nome atual): ")
                nova_senha = input("Digite a nova senha (ou pressione Enter para manter a senha atual): ")

                usuario.nome = novo_nome if novo_nome else usuario.nome
                usuario.senha = nova_senha if nova_senha else usuario.senha
                repository.salvar_usuario(usuario)
                print("Dados do usuário atualizados com sucesso!")
            else:
                print("Usuário não encontrado.")
        
        elif opcao == "4":
           
            email = input("Digite o e-mail do usuário que deseja excluir: ")
            usuario = repository.pesquisar_usuario(email)
            if usuario:
                repository.excluir_usuario(usuario)
                print("Usuário excluído com sucesso!")
            else:
                print("Usuário não encontrado.")
        
        elif opcao == "5":
            
            print("\nListando todos os usuários cadastrados:")
            lista_usuarios = repository.listar_todos_usuario()
            if lista_usuarios:
                for usuario in lista_usuarios:
                    print(f"Nome: {usuario.nome} - Email: {usuario.email} - Senha: {usuario.senha}")
            else:
                print("Nenhum usuário cadastrado.")
        
        elif opcao == "0":
            print("Saindo do sistema...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    os.system("cls || clear")
    main()
