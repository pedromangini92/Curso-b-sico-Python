km = float(input('Digite quantos KM terá a sua viagem:'))
km1 = km*0.50
km2 = km*0.45
if km <= 200:
    print('O valor da sua passagem é {}'.format(km1))
else:
    print('O valor da sua passagem é {}'.format(km2))
