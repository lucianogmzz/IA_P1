año = int(input("ingrese el año: "))

if año < 1582:
    print("no esta dentro del periodo gregoriano")
else:
    if año % 4 != 0:  #si el año no es divisible entre 4, es año comun
        print("año comun")
    elif año %100 != 0:  #si el año es divisible entre 4, pero no entre 100 es bisiesto
        print("año bisiesto")
    elif año %400 !=0: #si el año es divisible entre 100, pero no entre 400 es comun
        print("año comun")
    else:        # si es divisible entre 400, es bisiesto 
        print("año bisiesto")