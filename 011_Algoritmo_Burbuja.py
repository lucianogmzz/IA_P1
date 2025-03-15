list = []
swapped = True

num = int(input("cuantos numeros quieres ordenar?\n "))

for i in range(num):
    val = float(input("ingresa el valor a la lista: "))
    list.append(val)
    
while swapped:
    swapped = False 
    for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
            swapped = True
            list[i], list[i + 1] = list[i + 1], list[i]
        
print("lista ordenada:\n ", list)
