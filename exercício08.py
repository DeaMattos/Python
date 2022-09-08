#Escreva um programa que leia um valor em metros e exiba a tela o valor convertido em centímetros e em milímetros.

m = float(input('Valor em metros:'))
cm = m * 100
mm = m * 1000
print('A medida de {}m corresponde a {:.0f}cm e a {:.0f}mm.'.format(m, cm, mm))
