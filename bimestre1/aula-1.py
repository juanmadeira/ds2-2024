# 1
print("Python  demais!")

# 2
nome_completo = "Juan"
idade = "18"

print("Me chamo", nome_completo, "e tenho", idade, "anos.")

# 3
a = int(input("Digite um valor inteiro:"))
b = int(input("Digite outro valor inteiro:"))

print("{a} + {b} = {soma} \n{a} - {b} = {subtracao} \n{a} * {b} = {multiplicacao} \n{a} / {b} = {divisao}".format(a=a,b=b, soma=a+b, subtracao=a-b, multiplicacao=a*b, divisao=a/b))

# 4
nome = input("Insira o nome:")
sobrenome = input("Insira o sobrenome:")

nome_completo = (nome + " " + sobrenome)
print(nome_completo)

# 5
caractere = input("Insira um caractere:")
print("O caractere digitado foi", caractere)

# 6
idade = int(input("Insira a idade:"))
anoAtual = int(input("Insira o ano atual:"))

anoNasc = anoAtual - idade
anoPreAniversario = anoNasc - 1

print("O ano de nascimento do usuário caso já tenha feito aniversário é "+ str(anoNasc) +". Caso não tenha feito aniversário, o ano de nascimento é "+ str(anoPreAniversario) +".")

# 7
numero = int(input("Insira um número:"))

print("O antecessor do número inserido é {antecessor} e o seu sucessor é {sucessor}".format(antecessor = numero - 1, sucessor = numero + 1))