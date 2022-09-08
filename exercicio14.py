#Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.

c = float(input('Informe a temperatura em ºC:'))
f = 9 * c / 5 + 32 #neste caso, não é necessário o uso de parênteses pois a expressão já está na ordem de precedência.
print('A temperatura de {}ºC correspondea {}º F.'.format(c, f))