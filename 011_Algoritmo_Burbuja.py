list = []

num = int(input("cuantos numeros quieres ordenar?\n "))

for i in range(num):
    val = float(input("ingresa el valor a la lista: "))
    list.append(val)
    
list.sort()
print(list)