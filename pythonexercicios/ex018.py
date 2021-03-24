import math
a = float(input('Digite um angulo:'))

sen = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tan = math.tan(math.radians(a))

print('O seno do angulo é {:.1f}, tangente {:.1f} e o cosseno é {:.1f}'.format(sen, tan, cos))
