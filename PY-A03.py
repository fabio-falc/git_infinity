# [PY-A03] Crie um programa em Python que permita adicionar, remover e visualizar alunos e seus números de matrícula usando um dicionário.
# O programa deve fornecer as seguintes funcionalidades:
# Adicionar um aluno: O usuário poderá adicionar o nome e o número de matrícula de um aluno ao dicionário.
# Remover um aluno: O usuário poderá remover um aluno do dicionário informando o número de matrícula.
# Visualizar todos os alunos: O usuário poderá visualizar todos os alunos registrados no dicionário, exibindo seus respectivos números de matrícula.
# O programa deve ser executado em um loop contínuo até que o usuário escolha sair.



alunos = {}


while True:
    print('------    MENU    ------\n')
    print('1 - Cadastrar Aluno')
    print('2 - Remover Aluno ')
    print('3 - Visualizar todos Alunos: ')
    print('0 - Sair')  

    opcao = (input('\nSelecione uma opção: '))

    if opcao == '1':
        nome = input('Digite o nome do aluno: ')     
        matricula = input('Digite a matrícula do aluno: ')
        if matricula in alunos:
            print('Matrícula já cadastrada!')

        else:
            alunos[matricula] = nome 
            print('Aluno cadastrado com sucesso!\n')   

    elif opcao == '2':

        matricula = input('Digite a matrícula a ser removida: ')
        if matricula in alunos:
            del alunos[matricula]
            print('Aluno removido com sucesso!\n')
        else:
            print('Matricula não encontrada!')

    elif opcao == '3':
        
        if not alunos:
            print('Nenhum aluno cadastrado!')
        else:
            print('\nLista de alunos:')
            for matricula, nome in alunos.items():
                print(f'Matrícula: {matricula} Aluno: {nome}')  
       
    elif opcao == '0':
        print('Saindo do programa...')
        break

    else:
        print('Opção inválida! Tente novamente.')    

