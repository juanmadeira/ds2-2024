# Juan Madeira e Miguel Martins
# Turma 4C
# Prova de Python 1º bimestre (prática)

# declaração de variáveis
long_ini = float(input('Insira a longitude inicial (em graus):'))
long_end = float(input('Insira o ponto do destino (em graus):'))
spd = float(input('Insira a velocidade do navio pirata (em km/h):'))

# conversão pra km
long_km = long_end-long_ini

# distância percorrida por dia
spd_day = spd*24

# distância em graus percorrida por dia
long_deg = float(spd_day/111)

# primeiro movimento
pos_day = long_ini + long_deg

# primeiro dia
day=1

if spd == 0: # se a velocidade for zero
    print("O navio pirata não sai do lugar UwU.")
else:
    while pos_day < long_end: # grau alcançado no fim do dia
        print("No final do dia",day,"a posição do navio é {pos:.2f} graus de longitude.".format(pos = pos_day))
        pos_day += long_deg
        day+=1
    # destino
    print("No final do dia",day,"a posição do navio é {long:.2f} graus de longitude.".format(long = long_end))