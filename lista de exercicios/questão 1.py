vetor = []

N= int(input("Quantos números terá o vetor? "))

for i in range(N):
    num = int(input("escreva um número: "))
    vetor.append(num)

busca = int(input("Qual número deseja procurar? "))

contador = vetor.count(busca)

print("O número", busca, "aparece", contador, "vezes no vetor.")
