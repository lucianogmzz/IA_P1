my_tuple = (1, 10, 100)  # se declara una tupla

t1 = my_tuple + (1000, 10000) #se declaran otras dos tuplas, basandose en la tupla original
t2 = my_tuple * 3
#se imprime la extension de la tupla y las tuplas modificadas
print(len(t2))  
print(t1)
print(t2)
#se imprime el "esta" o "no esta" en la tupla 
print(10 in my_tuple)
print(-10 not in my_tuple)
