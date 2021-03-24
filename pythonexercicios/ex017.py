import math

c1 = float(input('Digite o cateto adjascente:'))
c2 = float(input('Digite o cateto oposto:'))
h = math.hypot(c1, c2)

print('A hipotenusa é {}'.format(h))