print('Bem Vindo ao simulador de empréstimos, digite a baixo os valores!')
casa = float(input('Qual é o valor da casa?'))
salario = float(input('Qual é o seu salário?R$'))
anos = int(input('Em quantos anos voce deseja pagar?'))
parcela = casa/(anos*12)
porcentagem = salario*.3
if parcela > porcentagem:
    print('Infelizmente o empréstimo ultrapassa 30% do seu salário, portanto não pode ser aprovado!!')
else:
    print('Parabéns, seu emprestimo foi aprovado\nFicará {} parcelas de R${:.2f}'.format(anos*12, parcela))
