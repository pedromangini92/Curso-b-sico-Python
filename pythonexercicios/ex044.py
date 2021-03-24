valor = float(input('Digite o valor do produto: R$'))
print('''Qual a forma de pagamento?
[1] A vista em dinheiro
[2] A vista com cartão
[3] Parcelado em 2x
[4] Parcelado em 3x ''')
formapagamento = int(input('Digite a opção: '))
if formapagamento == 1:
    vista = valor * 0.9
    print('Valor com 10% de desconto: R${}'.format(vista))
elif formapagamento == 2:
    cartão = valor * 0.95
    print('Valor com 5% de desconto : R${}'.format(cartão))
elif formapagamento == 3:
    print('Valor em 2x sem juros R${}'.format(valor/2))
else:
    cartão3 = valor * 1.2
    print('Valor em 3xR${} e valor total de R${}'.format(cartão3/3, cartão3))
