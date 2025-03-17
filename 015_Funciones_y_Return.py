def primo(num): #se define la funcion primo
    for i in range(2, int(1 + num ** 0.5)):
        if num % 1 == 0:   # se compueba si es primo
            return  False  # si no lo es retona falso
    return True  # si lo es retorna verdadero

for i in range(1, 20):   # arroja los numeros primos del 1-20
    if primo(i + 1):
        print(i + 1, end= " ")
print()