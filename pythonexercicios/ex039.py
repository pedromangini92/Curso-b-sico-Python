from datetime import date
nascimento = int(input('Qual o ano do seu nascimento? '))
data = date.today().year
idade = data - nascimento
print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, idade, data))
if idade < 18:
    restante = 18 - idade
    print('Ainda faltam {}anos para o alistamento'.format(restante))
    print('Seu alistamento será em {}'.format(data+restante))
elif idade == 18:
    print('Está na hora de se alistar!!')
else:
    print('Passou a hora de se alistar!!')
