notas = []

contador = 1

while contador <= 5:
    cod = input("RM: ")
    nota = float(input("NOTA: "))
    resultado = [cod, nota]
    notas.append(resultado)


    # alternativa: contador += 1
    contador = contador + 1

print( 'quantidade de notas', len(notas) )