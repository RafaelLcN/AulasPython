# len = quantos elementos possui na lista
#  "+" utilizado para juntar duas ou mais listas
# "*" utilizado para repetição
# "in" utilizado para verificar se há um elemento x na lista
# "for x in [1,2,3] : print (x, end='')"


# Valores mínimos, máximos e soma em listas
# "min" é utilizado para verificar o menor valor na lista
# "max" é utilizado para verificar o maior valor na lista
# "sum" é utilizado para somar todos os valores da lista

idade = [10, 11, 15, 17, 9, 8, 11, 15, 14, 12, 12, 10, 15, 13, 10, 13, 15, 10, 16, 16, 10, 11, 13, 14, 12, 15, 14, 15, 14, 17]
alturas = [1.50, 1.55, 1.60, 1.65, 1.70, 1.75, 1.80, 1.85, 1.90, 1.95, 2.00, 1.52, 1.57, 1.62, 1.67, 1.72, 1.77, 1.82, 1.87, 1.92,
    1.54, 1.59, 1.64, 1.69, 1.74, 1.79, 1.84, 1.89, 1.94, 1.98]

n = 0
text = ''
min_list = min(len(idade), len(alturas))
while n < min_list:
    text += '\nO aluno {} possui {} de altura'.format(idade[n], alturas[n])
    n += 1
print(text)

soma = sum(alturas)
media = soma / len(alturas)
print("A média de altura dos alunos é:", media)

cont = 0
for i in range(len(idade)):
    if idade[i] > 13 and alturas[i] < media:
        cont += 1

print("Número de alunos com mais de 13 anos e altura inferior à média:", cont)



