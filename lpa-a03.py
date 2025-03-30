# [LPIA-A03] Você está criando um programa em Python para simular um jogo simples de adivinhação. O programa deve ter um número fixo, por exemplo, 7, que o jogador deve adivinhar. O jogador terá até 3 tentativas para acertar o número.

# Implemente o jogo utilizando um loop while para permitir que o jogador faça múltiplas tentativas até acertar ou atingir o limite de tentativas. Utilize a estrutura else para exibir uma mensagem de encorajamento caso o jogador acerte e uma mensagem de consolo caso as 3 tentativas se esgotem sem sucesso.

cont = 0
lucky_number = 7


while cont < 3:
    
    number = int(input('Adivinhe o número: '))

    if number != lucky_number:
        cont += 1
        print(f'Número incorreto! Tentativas restantes {3 - cont}')
    else:
        print('Parabéns você acertou! ')
        break       
    
if cont == 3 and number != lucky_number:
    print('Número de tentativas excecidas! Inicie o programa novamente. ')        