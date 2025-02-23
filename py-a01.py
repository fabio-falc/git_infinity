#[PY-A01] Faça um programa em python que determine em duas variáveis (senha e email) e que contenha uma senha e um email cadastrados antecipadamente, em seguida solicite ao usuário uma senha e um email e utilize o laço de repetição juntamente com a estrutura de condição para verificar se o email e a senha digitado pelo usuário é igual ao email e senha cadastrados antecipadamente. E enquanto a senha e o email que o usuário digitou não for igual ao email e senha cadastrados ele continue em um loop.

#cadastro de email e senha
# determine email e senha
# laço de repetição, e estrutura condicional
# 

print('\n---------------------------------------------')
print('---------- CADASTRO EMAIL e SENHA -----------')
print('---------------------------------------------\n')


while True:
    email_cadastro = input('Digite um email para cadastro: ')
    if '@' in email_cadastro and '.' in email_cadastro:
        break
    else:
        print('Digite um email valido.')
senha_cadastro = input('Digite uma senha para cadastro: ')

print('\n---------------------------------------------')
print('---                 LOGIN                 ---')
print('---------------------------------------------')


while True:
    email = input('\nDigite o email cadastrado: ')
    senha = input('Digite a senha cadastrada: ')

    if email == email_cadastro and senha == senha_cadastro:
        print('\nLogin efetuado com sucesso.')
        print('\tSeja Bem-vindo! ')
        break    
    else:
        print('\nEmail ou Senha incorreta, Digite novamente.')
        print('\n---------------------------------------------')
        print('---                 LOGIN                 ---')
        print('---------------------------------------------')
