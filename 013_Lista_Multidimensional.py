# Definir las dimensiones del hotel
edificios = 3
pisos = 15
habitaciones = 20

# Crear una estructura de datos para almacenar la ocupación del hotel
# Se usa una lista tridimensional con valores False (todas las habitaciones están inicialmente libres)
hotel = [[[False for _ in range(habitaciones)] for _ in range(pisos)] for _ in range(edificios)]

# Solicitar al usuario que seleccione una habitación
edificio = int(input("Ingrese el número de edificio (1-3): ")) - 1
piso = int(input("Ingrese el número de piso (1-15): ")) - 1
habitacion = int(input("Ingrese el número de habitación (1-20): ")) - 1

# Validar que los valores ingresados estén dentro del rango permitido
if 0 <= edificio < edificios and 0 <= piso < pisos and 0 <= habitacion < habitaciones:
    print(f"La habitación seleccionada en Edificio {edificio + 1}, Piso {piso + 1}, Habitación {habitacion + 1} está {'Ocupada' if hotel[edificio][piso][habitacion] else 'Libre'}.")
else:
    print("Error: Número de edificio, piso o habitación fuera de rango.")
