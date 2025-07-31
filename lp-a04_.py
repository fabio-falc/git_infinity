"""
[LP-A04] Escreva um programa em python que leia números inteiros do teclado. O programa deve ler os números até que o usuário digite 0 (zero). No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética.

"""

print("=== Programa de números ===\n")

# Variáveis criadas para armazenar os valores
qtd_numeros = 0
soma = 0
numeros_digitados = [] # array dos números digitados


while True: # loop até que digite "0"
    try:
        numero = int(input("Digite um número: ")) # entrada de dados
    except ValueError:
        print("Entrada inválida. Digite apenas números inteiros.")
        continue
    
    # estrutura condiconal que se dif. de "0", soma a qtd digitadas, assim como os números e isere os valores em um array
    if numero != 0: 
        qtd_numeros += 1
        soma += numero
        numeros_digitados.append(numero)

    # Caso digitado "0": calcula a média, e exibe os dados pedidos no programa
    else:    
        if qtd_numeros > 0:
            media = soma / qtd_numeros
        else:
            media = 0    
        print("Fim ...")
        print(f"Quantidade de números digitados: {qtd_numeros}")
        print(f"Soma total: {soma}")
        print(f"Média: {media:.1f}")
        print(f"Números digitados: {numeros_digitados}")
        break # fim

