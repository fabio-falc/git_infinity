
print("========== SISTEMA de LOGIN ==========")

                    # Cadastro e verificação de login

login_cadastro = input("\nDigite o login para cadastro: ")
while True:
    confirma_login = input("Digite o login para confirmação: ")

    print("=" * 40)
    if confirma_login != login_cadastro:
        print("\nLogins não coincidem com anterior, digite novamente!") 
    else:      
                    # Cadastro e verificação de senha

        senha_cadastro = input("Digite uma senha para cadastro: ")

        while True:

            senha_confirmacao = input ("\nDigite novamente a sua senha: ")   

            if senha_confirmacao != senha_cadastro:

                print("Senhas não coincidem, digite novamente.")  

            else:
                
                print("Cadastro realizado com sucesso.\n")
                break
        break        


print("=========== Login ===========")

tentativa_login = 3
while tentativa_login > 0:
    print("=" * 40)
    confirma_login = input("Digite o seu login: ")
    senha = input("Digite a sua senha: ")

    if (confirma_login == login_cadastro) and (senha == senha_cadastro): 
        print(f"Bem-Vindo {confirma_login}")
        break
    else:
        tentativa_login -= 1    
        print(f"\nLogin/Senha incorreto.\nTentativas restantes {tentativa_login} ")

        # caso número de tentativas 0 
        if tentativa_login == 0:
            print("\n")
            print("=" * 40)
            for _ in range(3):
                                
                print("Acesso bloqueado!")







