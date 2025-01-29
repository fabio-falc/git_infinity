# [LP-A02] Escreva um programa em python que pergunte ao usuário a velocidade de um carro. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado e o valor da multa, cobrando R$20,00 por cada km que exceder 80 km/h.

print('\n=== Programa para Velocidade e Multa ===\n')

velocidade = float(input('Digite a velocidade em Km/h: '))

if velocidade > 80:
    multa = (velocidade - 80) * 20
    print(f'Sua velocidade foi {velocidade:.2f}Km/h e está acima do limite permitido, sua multa é R$ {multa:.2f}'  )
else:
    print(f'Sua velocidade é {velocidade:.2f}Km/h , está dentro do limite.')    
print('=========================================')    