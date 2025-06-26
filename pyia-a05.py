"""
[PYIA-A05] Crie uma função chamada maior_numero que receberá três números como argumentos. Esta função deve comparar os três números e identificar qual deles é o maior. Para isso, utilize uma estrutura de controle que verifique qual número é maior que os outros dois. A função deve então retornar o maior número encontrado.


"""


def maior_numero(num1, num2, num3):


    if num1 >= num2 and num1 >= num3:
        return num1

    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3 
    

# Entrada de dados

try:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    num3 = int(input("Digite o terceiro número: "))
    
    # Chamada da função

    numero_maior = maior_numero(num1, num2, num3)

    # Saída formatada

    print(f"O maior número é: {num1}, {num2} e { num3} é: {numero_maior}")

except ValueError:
    print("Por favor, digite apenas números inteiros válidos.")   