#Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de diad pelos quais ele foi alugado. Calcule o preço a pagar sabendo que o carro cista R$ 60,00 por dia e R$0,15 por km rodado

k = float(input('Quantos KM você percorreu? Km'))
d = int(input('Número de diárias: '))
vd = d * 60
vk = k * 0.15
s = vd + vk
print('Km percorridos: {}km - Custo R${:.2f} \nNúmero de diárias:{} - Custo R${:.2f} \nTotal a ser pago: R${:.2f}'.format(k, vk, d, vd, s))
