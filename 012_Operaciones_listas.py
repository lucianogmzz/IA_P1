# Lista original con números repetidos
numeros = [1, 2, 3, 2, 4, 5, 1, 6, 3, 7, 8, 5]

# Crear una lista nueva sin duplicados
numeros_sin_duplicados = []
for num in numeros:
    if num not in numeros_sin_duplicados:
        numeros_sin_duplicados.append(num)

# Imprimir la lista sin duplicados
print("Lista original:", numeros)
print("Lista sin duplicados:", numeros_sin_duplicados)
