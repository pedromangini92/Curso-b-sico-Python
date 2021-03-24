import random
l1 = [0,1,2,3]
n1 = random.choice(l1)
n2 = int(input('Tente adivinhar qual o numero entre 0 e 5 que o computador escolheu:'))
if n2 == n1:
    print('Parabens voce acertou!!!')
else:
    print('Voce chegou perto, tente novamente')
