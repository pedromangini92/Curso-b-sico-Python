n1 = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para hexadecimal''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(n1, bin(n1) [2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(n1, oct(n1)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(n1, hex(n1)[2:]))
else:
    print('OPÇÃO INVÁLIDA!!!')
