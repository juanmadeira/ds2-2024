# 1
nome = input("Insira o nome do vendedor:")
salarioInicial = float(input("Insira o salário do vendedor (em R$):"))
totalVendas = float(input("Insira o total de vendas (em R$):"))

salarioFinal = salarioInicial + (totalVendas * 0.15)

print("A remuneração final de", nome, "é de R$", salarioFinal)

# 2
t = input("Insira o tempo gasto na viagem (em horas):")
v = input("Insira a velocidade média durante a viagem (km/h):")
d = float(v) * float(t)
consumo = d/12

print("A quantidade de gasolina é de", consumo, "litros")