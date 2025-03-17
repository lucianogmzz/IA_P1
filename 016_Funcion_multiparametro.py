def bmi(peso, altura):   #se define la funcion bmi
    if peso < 1.0 or altura > 2.5 or \
    peso < 20 or peso > 200:  #utiliza salto de linea  y hace comprobacion que datos esten en el rango
        return None

    return peso / altura ** 2


print(bmi(352.5, 1.65))  #imprime la funcion con los parametros requeridos
