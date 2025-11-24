A = []
B = []
C = []  # VETOR INTERCALADO

print("vetor A: ")
for i in range(5):
    A.append(int(input("escreva um número: ")))


print("\nvetor B: ")
for i in range(5):
    B.append(int(input("escreva um número: ")))


for i in range(5):
    C.append(A[i])
    C.append(B[i])

print("\nVetor intercalado:")
print(C)