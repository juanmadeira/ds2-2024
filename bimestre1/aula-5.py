# 1
def menorNumero(n, n1):
    menor = n

    if(n1 < menor):
        menor = n1

    elif(n1 == menor):
        return print('Os números são iguais.')

    return print('O menor número é o ', menor)


n = input('Insira o primeiro número: ')
n1 = input('Insira o segundo numero: ')

menorNumero(n, n1)

# 2
def positivoNumero(n):
    if(n > 0):
        return print('O número é positivo')

    elif(n < 0):
        return print('O número é negativo')

    elif(n == 0):
        return print('O número não é positivo nem negativo')


n = int(input('Insira um número: '))

positivoNumero(n)

# 3
def limiteFunc(a, b, limite):
    if (a + b) > limite:
        return True

    else:
        return False


a = input('Insira o primeiro número: ')
b = input('Insira o segundo número: ')

limite = input('Insira o parâmetro limite:')

print(limiteFunc(a, b, limite))

limiteFunc(a, b, limite)

# 4
def fizzBuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        print('FizzBuzz')

    elif n % 3 == 0:
        print('Fizz')

    elif n % 5 == 0:
        print('Buzz')


n = int(input('Insira um número: '))

fizzBuzz(n)

# 5
def lista(n):
    flag = False
    k = []
    c = 0
    while c != -1:
        c = float(
            input('Digite um número para sua lista (digite -1 para finalizar):'))
        if (c != -1):
            k.append(c)

    for x in k:
        if x == n:
            flag = True

    return flag


n = float(input('Insira um número como parâmetro:'))
print(lista(n))

# 6
def somaInteirosMenores(n):
    soma = 0
    for x in range(n + 1):
        soma += x

    return soma


n = int(input('Insira um número inteiro e positivo: '))

somaInteirosMenores(n)