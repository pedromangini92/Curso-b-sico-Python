from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint (0,2)
print('''Suas opção são:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual a sua opção?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('-=' *15)
print('O computador escolheu {}'.format(itens[computador]))
print('O jogador escolheu {}'.format(itens[jogador]))
print('-=' *15)
if computador == 0:
    if jogador == 0:
        print('EMPATOU')
    elif jogador == 1:
        print(' JOGADOR GANHOU')
    else:
        print(' COMPUTADOR GANHOU')
elif computador == 1:
    if jogador == 0:
        print(' COMPUTADOR GANHOU')
    elif jogador == 1:
        print('EMPATOU')
    else:
        print(' JOGADOR GANHOU')
elif computador == 2:
    if jogador == 0:
        print(' JOGADOR GANHOU')
    elif jogador == 1:
        print(' COMPUTADOR GANHOU')
    else:
        print('EMPATOU')
