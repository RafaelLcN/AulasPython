meses = []
temperaturas = []


for mes_num in range(1, 13):
    mes = input(f"Insira o nome do {mes_num}º mês: ")
    temperatura = float(input(f"Insira a média de temperatura para {mes}: "))

    meses.append(mes)
    temperaturas.append(temperatura)


print("\nMeses e Temperaturas Registrados:")
for mes, temp in zip(meses, temperaturas):
    print(f"Mês: {mes}, Temperatura: {temp}")


soma = sum(temperaturas)
media = soma / len(temperaturas)
print(f"A média de temperatura anual é: {media:.2f}")


print("\nTemperaturas acima da média anual:")
for mes, temp in zip(meses, temperaturas):
    if temp > media:
        print(f"Mês: {mes}, Temperatura: {temp:.2f}")
