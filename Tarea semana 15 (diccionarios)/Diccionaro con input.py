# Solicitar al usuario que ingrese los datos
nombre = input("Ingrese el nombre: ")

# Verificar que la edad sea un número entero válido
while True:
    try:
        edad = int(input("Ingrese la edad: "))
        break
    except ValueError:
        print("Por favor, ingrese un número válido para la edad.")

ciudad_inicial = input("Ingrese la ciudad actual: ")
nueva_ciudad = input("Ingrese la nueva ciudad: ")
profesion = input("Ingrese la profesión: ")
alergias = input("Ingrese las alergias (si tiene, si no tiene deje en blanco): ")
tipo_sangre = input("Ingrese el tipo de sangre: ")

# Crear un diccionario llamado informacion_personal con los datos ingresados
informacion_personal = {
    "nombre": nombre,
    "edad": edad,
    "ciudad": ciudad_inicial,
    "profesion": profesion,
    "alergias": alergias if alergias else "N/A",  # "N/A" si no ingresa alergias
    "tipo de sangre": tipo_sangre if tipo_sangre else "N/S"  # "N/S" si no especifica el tipo de sangre
}

# Acceder al valor asociado con la clave "ciudad" y modificarlo
informacion_personal["ciudad"] = nueva_ciudad  # Modificando la ciudad a la nueva ingresada

# Verificar si la clave "telefono" existe en el diccionario
telefono = input("Ingrese el número de teléfono (si no tiene, deje en blanco): ")
if telefono:
    informacion_personal["telefono"] = telefono  # Agregando el número de teléfono ingresado
else:
    informacion_personal["telefono"] = "N/T"  # "N/T" si no tiene teléfono

# Eliminar la clave "edad" del diccionario ya que no es necesaria más adelante
del informacion_personal["edad"]

# Imprimir el diccionario final después de todas las operaciones
print("\nDiccionario final:", informacion_personal)
