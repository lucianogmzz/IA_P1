school_class = {}  # se crea un diccionario vacio

while True:  # se inicia el bucle
    name = input("Ingresa el nombre del estudiante: ")  #se ingresa el nombre del alumno por parte del usuario
    if name == '':
        break #se sale del bucle si el nombre esta vacio
    
    score = int(input("Ingresa la calificación del estudiante (0-10): ")) # se ingresa la calificacion del alumno
    if score not in range(0, 11):
	    break  # si la calificacion no es de 0-10, abandona el bucle
 
    # si el nombre ya esta agregado se alarga la tupla
    #si el alumno es nuevo se crea una nueva tupla

    if name in school_class:
        school_class[name] += (score,)
    else:
        school_class[name] = (score,)

# se ordenan los nombres 
for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:      # se itera a traves de la tupla para tomar todas las calificaciones y sacar el promedio
        adding += score
        counter += 1
    print(name, ":", adding / counter)
