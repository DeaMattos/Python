#Faça um algoritmo que leia o salario de um funcionário e mostre o seu novo salário com 15% de aumento.

salario = float(input('Salário Bruto: R$'))
aumento = salario + (salario*15/100)
print('Após o reajuste de 15%, o salário passou de R${:.5f} para R${:.5f}.'.format(salario, aumento))
