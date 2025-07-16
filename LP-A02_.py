
def calcular_multa(velocidade): # funcao recebe parâmetro 'velocidade'
    limite = 80 # limite de velocidade
    valor_multa = 20 # valor aplicado a cada km excedido

    if velocidade > limite: # calculo da multa
        excesso = velocidade - limite
        multa = excesso * valor_multa
        # saida de dado caso velocidade seja maior
        print(f"\nSua velocidade foi {velocidade:.2f}Km/h - acima do limite!")
        print(f"Multa aplicada: R$ {multa:.2f}")
        #  saida de dado caso velocidade seja menor
    else:
        print(f"\n Sua velocidade foi {velocidade:.2f}Km/h - dentro do limite.")

# inicio do programa 
print("\n=== Programa para Velocidade e Multa ===\n")

try: # tratamento de erro
    velocidade = float(input("Digite a velocidade em Km/h: ")) # entrada de dado
    if velocidade < 0: # caso velocidade menor que 0 retorna o msg do erro
        print("Velocidade inválida. Digite um valor positivo")
    else: 
        calcular_multa(velocidade) # velocidade acima de 0 inicia a função
except ValueError:
    print("Entrada inválida. Digite um número  válido.")

print("=" * 50) # firula xD                