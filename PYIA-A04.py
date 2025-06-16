"""
Crie uma função chamada media que receberá três números como argumentos.
Esta função deve calcular a média aritmética desses três números. Para fazer isso, some os três números e, em seguida, divida o resultado por três. Por fim, a função deve retornar o valor da média aritmética calculada.

"""
# definição da função

def media(a, b, c): # Função recebe três parâmetros

    media_aritmetica = (a + b + c) / 3 # Cálculo da media arítmetíca


    return media_aritmetica # Retorna o valor


# Coleta de valores em float
num1 = float(input("Digite um valor: "))
num2 = float(input("Digite outro valor: "))
num3 = float(input("Digite outro valor: "))

resultado = media(num1, num2, num3) # variável retorna resultado da função

print(f"A média arítmética de {num1}, {num2} e {num3} é: {resultado:.2f}") # Mostra o resultado na tela