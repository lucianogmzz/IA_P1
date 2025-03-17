dictionary = {"cat": "gato", "perro": "chien", "caballo": "cheval"} # se define el diccionario
words = ['gato', 'león', 'caballo']  #palabras a buscar
 
for word in words:  # for para la iteracion y buscar las palabras
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "no está en el diccionario")   # si no estan las palabras
