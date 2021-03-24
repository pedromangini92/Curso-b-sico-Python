ano = int(input('Digite um ano para saber se ele pe bissexto:'))
bi = ano%4
if bi == 0 and bi % 100 != 0 or bi % 400 == 0:
    print('O ano de {} é um ano bissexto:'.format(ano))
else:
    print(' O ano de {} não é um ano bissexto:'.format(ano))
