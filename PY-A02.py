
lista = []
lista_pares = []
lista_impares = []

"""
Faça um programa que solicite ao usuário que digite 10 valores para preencher uma lista

"""

for numero in range (0,10):
    lista.append(int(input(f'Digite o {numero+1}° valor: ')))


"""
separar os números pares e ímpares em listas diferentes.
"""


for numero in lista:
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)  

tupla_par = tuple(lista_pares)
tupla_impar = tuple(lista_impares)

# Exiba na tela lista, quantidade e soma todos números pares

print('\n------     PARES     ------\n')
print(f'Lista de pares: {tupla_par}.')
print(f'A quantidade de números pares na lista é {len(lista_pares)}.')
print(f'A soma de todos os números pares é {sum(lista_pares)}.')

# Exiba na lista, quantidade e soma de todos os números impares

print('\n------     IMPARES     ------\n')
print(f'Lista de impares: {tupla_impar}.')
print(f'A quantidade de números impares na lista é {len(lista_impares)}.')
print(f'A soma de todos os números impares é {sum(lista_impares)}.')







