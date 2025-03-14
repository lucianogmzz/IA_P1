hor = int(input("inserta la hora de inicio (horas):"))
min = int(input("inserta minuto de inicio (minutos):"))
dur = int(input("inserta los minutos de duracion:"))

min = min + dur # suma de los minutos de inicio y la duracion
hor = hor + min //60 #encuentra la cantidad de horas y actualiza la variable

min = min % 60 # se utiliza el residuo para setear los min de 0-59
hor = hor % 24 # se utiliza el residuo para setear las horas de 0-23
print(hor, ":", min, sep="")