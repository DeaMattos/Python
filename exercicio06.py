#Crie um algorítmo que leia um número e mostre o seu dobro, triplo e sua raiz quadrada.

n = int(input('Digite um valor:'))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro de {} vale {}.'.format(n,d))
print('O triplo de{} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(n, t, n, r))
#Utilizamos a formatação das casas decimais entre as chaves correspondentes a operação aritmédica {:.2f}.

