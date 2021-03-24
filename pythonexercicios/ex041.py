from datetime import date
data = int(input('Digite o ano de nascimento do atleta: '))
data1 = date.today().year
ano = data - data1
if data >= 2011:
    print('Atleta Mirim')
elif data >= 2006 and data < 2011:
    print('Atleta Infantil')
elif data >= 2001 and data < 2006:
    print('Atleta Junior')
elif data >= 2000 and data < 2001:
    print('Atleta Senior')
else:
    print('Atleta Master')

