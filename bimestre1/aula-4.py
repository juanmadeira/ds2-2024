# 1
idade = int(input('Digite sua idade'))
if idade >= 18:
    print('Você é maior de idade!')
else:
    print('Você é menor de idade.')

# 2
animal = input('Digite o nome de um animal').lower()
match animal:
    case 'gato':
        print('O animal é um gato.')
    case 'cachorro':
        print('O animal é um cachorro')
    case _:
        print('O animal não é um gato nem um cachorro')

# 3
for x in range(1, 101):
    if x%2 != 0:
        print(x)

# 4
k = []
c=0
while c!=-1:
    c = float(input('Digite um número para sua lista (digite -1 para finalizar)'))
    if (c!=-1):
        k.append(c)
print(k)
media = 0
for x in k:
    media +=x
media = media/len(k)
print('A lista de números criada é:',k)
print('A média dos números listados é',media)

# 5
n = 0
while n <= 0 and n % 1 == 0:
    n = int(input('Digite um número'))

soma = 1
for i in range(2, n + 1):
    soma += 1/i

print(soma)

# 6
for x in range(1000,2001):
    if x%11==5:
        print(x)
