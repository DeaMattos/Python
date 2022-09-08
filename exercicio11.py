#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

h = float(input('Altura da parede em metros:'))
w = float(input('Largura da parede em metros:'))
a = h * w
t = a / 2
print('A área de {:.2f} x {:.2f} é de {:.2f}.'.format(h, w, a))
print('Será necessário {:.2f}l de tinta para uma demão.'.format(t))
