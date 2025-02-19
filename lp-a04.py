print('=== Cadastro de senha e usuário ===')




cadastro_senha = int(input('Cadastre uma senha: '))


for tentativas in range (3, 0, -1):
    senha = int(input('Confirme a sua senha: '))
    if senha == cadastro_senha:
        print('Bem-vindo!')
        break
    else:
        
        print(f'Senha incoreta. Tentativas restantes {tentativas - 1}')
    if tentativas - 1 == 0:
        print('Número de tentativas excedidas, usuario bloqueado.')        