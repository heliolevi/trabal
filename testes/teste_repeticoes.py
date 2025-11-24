salarios = [] # lista geral

for x in range(4):
    nome = input("Nome? ")
    valor=float(input("Quanto você desjear solicitar? "))
    resultado=[nome, valor]
    salarios.append(resultado)

print("\nQuantidade solicitada por cada usuario:\n")

for v in salarios:
    nome = v[0]
    valores = v[1]
    print("O usuario", nome,
           "tirou a nota", valores)