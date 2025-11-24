print("primeira aula") # print é tudo que eu quero que exiba

'Vamos aprender variavel'

# boolean
is_python = True
is_java = False

# armazenando condições
passaportes = 30
comprdores = 250
temos_passaporte_suficiente = (passaportes >= comprdores)
print(temos_passaporte_suficiente)

# vamos aprender sobre como pegar um dado 

nome = input("Qual seu nome? ") #Porem o input ele retorna tdo como strin (texto)
idade = int( input("Qual sua idade? ") )
peso = float( input("Qual seu peso? ") )


# Operadores

soma = 1 + 1
multiplicacao = 4 * 4
divisao = 30 / 3
potencia = 7 ** 2

print("soma", soma)
print("multiplicação", multiplicacao)
print("divisão", divisao)
print("Potência", potencia)


# CONDIÇÕES 

idade = int(input(" Qual sua idade? "))

if idade >= 18: 
    print("PERMITIDO!")
else:
    print("BLOQUEADO!")


# LISTAS

numero = [1,2,3,4,5,6]

numero[0]=8

print(numero[0])

print("total", len(numero))
print("máximo", max(numero))
print("minimo", min(numero))
