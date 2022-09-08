#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere US$ 1.00 = R$3.27

real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 3.27
print('Com R$ {:.2f} você poder comprar US$ {:.2f}.'.format(real, dolar))

#Programa onde o usuário informa o valor para investimento e o valor da cotação

real = float(input('Quanto você tem de dinheiro na carteira? R$'))
euro = float(input('Em quanto está a cotação do Euro hoje? ERU$'))
resultado = real / euro
print('Com R$ {:.2f} você pode comprar ERU$ {:.2f}.'.format(real, resultado))

