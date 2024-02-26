# 1
bool("abc")
bool(range(0))
bool(123456.789)
bool(-5)
bool(None)
bool(not(False))
bool(False)
bool(print())

# 2
vendas = [
    ["camisetas", 20, int(input("Informe quantas camisetas vendidas: "))],
    ["calcas", 50, int(input("Informe quantas calças vendidas: "))],
    ["sapatos", 100, int(input("Informe quantos sapatos vendidos: "))]
]

totCamisetas = vendas[0][1] * vendas[0][2]
totCalcas = vendas[1][1] * vendas[1][2]
totSapatos = vendas[2][1] * vendas[2][2]

totGeral = totCamisetas + totCalcas + totSapatos
print("O total de vendas de camisetas foi de R${camisetas:.2f}\nO total de vendas de calças foi de R${calcas:.2f}\nO total de vendas de sapatos foi de R${sapatos:.2f}\nO total de vendas no geral foi de R${geral:.2f}".format(camisetas = totCamisetas, calcas = totCalcas, sapatos = totSapatos, geral = totGeral))