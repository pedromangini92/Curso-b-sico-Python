salario = float(input('Qual o seu salario?R$'))
s1 = salario*1.1
s2 = salario*1.15
if salario > 1250:
    print('Você ganhou 10% de aumento, seu salario agora é R${:.2f}'.format(s1))
else:
    print('Você ganhou 15% de aumento, agora seu salario é R${:.2f}'.format(s2))
