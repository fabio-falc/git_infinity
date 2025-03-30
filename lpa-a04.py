# [LPIA-A04] Você está desenvolvendo um programa em Python para calcular a soma dos números pares dentro de um intervalo determinado pelo usuário. O programa deve solicitar ao usuário que insira dois números inteiros, representando o início e o fim do intervalo (inclusive).

# Utilize um loop 'for' para iterar sobre todos os números no intervalo e somar apenas os números pares. Implemente a estrutura 'else' para exibir uma mensagem indicando que não há números pares no intervalo, caso seja o caso.

# Ao final, exiba a soma dos números pares encontrados.

start = int(input('Digite um número para iniciar: '))
stop = int(input('Digite um número para finalizar: '))


soma_par = 0
for i in range(start,stop + 1):

    #number = int(input('Digite um número: '))

    if i % 2 == 0:
        soma_par  += i  


if soma_par > 0:

    print(f'A soma dos números pares são : {soma_par}')        

else:
    print('Não há números pares no intervalo')    