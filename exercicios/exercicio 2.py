# Peça 10 números. Depois imprima:

numeros = []

for x in range(10):
    numero = float(input("escreva um numero? "))
    numeros.append(numero)

print("\nTotal:", len(numeros))
print("Máximo:", max(numeros))
print("Mínimo:", min(numeros))
print("Soma:", sum(numeros))
print("Média:", sum(numeros) / len(numeros))