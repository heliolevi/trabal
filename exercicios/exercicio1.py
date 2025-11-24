# Peça 5 nomes e 5 notas. No final, mostre:

nomes = []

for x in range (5):
    nome = input("Qual é seu nome? ")
    nota = float(input("Qual foi sua nota? "))
    resultado  = [nome, nota]
    nomes.append(resultado)

print("Resultados: ")
for pessoa in nomes:
    print(pessoa[0], "tirou", pessoa[1])