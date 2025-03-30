
# [LPIA-A05]Desenvolva um programa em Python para calcular a média de notas de alunos em uma disciplina. O programa deve solicitar ao usuário o número de alunos e, em seguida, para cada aluno, pedir o nome e três notas. Utilize um loop 'for' para iterar sobre os alunos e suas notas.

# Além disso, implemente uma estrutura condicional para verificar se cada aluno foi aprovado ou reprovado, considerando que a média mínima para aprovação é 7.0. Exiba o nome do aluno, suas notas, média e a indicação de aprovação ou reprovação.

# Ao final, exiba a média geral da turma.

soma_medias = 0

# quantidade de alunos

alunos_qte = int(input('Digite a quantidade de alunos: '))

# Nome e  três notas

print()
for aluno in range(alunos_qte):
    nome = input('Digite o nome do aluno: ')

    soma_nota = 0
    for i in range(3):
        notas = float(input(f'Digite a {i+1}° nota de {nome}: '))
        soma_nota += notas

    media = soma_nota / 3
    soma_medias += media

    if media >= 7.0:
        situacao = 'APROVADO'
    else:
        situacao = 'REPROVADO'    

    print(f'\nAluno: {nome}')
    print(f'Média: {media:.1f}')
    print(f'Situação: {situacao}\n')  

media_geral = soma_medias / alunos_qte
print(f'Média Geral da Turma: {media_geral:.1f}\n')      