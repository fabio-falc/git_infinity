print("=== NÚMEROS INTEIROS ===")


soma = 0
quantidade = 0
while True:
    numero = int(input("Digite um número: "))
    if numero == 0:
        break
    else:
        soma += numero
        quantidade += 1

print("========================")
print(f"\nNúmeros digitados: {quantidade}")
print(f"Soma total: {soma}")
if quantidade != 0:
 media = soma / quantidade
 print(f"Média Aritimética: {media:.2f}")
print("========================")


