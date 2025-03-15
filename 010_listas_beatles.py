beatles =[]  #paso 1 crear lista de beatles
print("paso 1: ", beatles)

#paso 2, agregar con append a los miembros fundadores
beatles.append("John Lennon")
beatles.append("George Harrison")
beatles.append("Paul Mcartney")
print("paso 2: ", beatles)

#paso 3, agregar miembros no oficiales con ciclo for

for i in["Stu Sutcliffe", "Pete Best"]:
    miembro = input(f"agrega a:  {i}")
    beatles.append(miembro)
print("paso 3: ", beatles)

#paso 4, eliminar a los miembros no oficiales con del

for _ in range(2):
    del beatles[-1]
print("paso 4: ", beatles)

#paso 5 agregar a ringo

beatles.insert(0, "Ringo Star")
print("paso 5: ", beatles)
