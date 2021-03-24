velocidade = float(input('Qual foi a velocidade do carro?'))
multa = (velocidade-80)*7
if velocidade >80:
    print('Voce foi multado!!! \nE sua multa iré custar R${}'.format(multa))
