bloques = int(input("ingresa el numero de bloques"))
altura = 0
bloques_uso = 0

while bloques_uso + (altura + 1) <= bloques:  
    altura += 1  #aumenta la altura
    bloques_uso += altura  #bloques requeridos para el nivel
    
print("la altura de la piramide es: ")