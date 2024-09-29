# Crear un diccionario llamado informacion_personal con datos ficticios de una persona
informacion_personal = {
    "nombre": "Nayely Ayala Alarcon",
    "edad": 22,
    "ciudad": "Babahoyo",
    "profesion": "Azafata",
    "alergias": "Ampicilina",  # Información adicional sobre alergias
    "tipo_sangre": "O+"  # Información adicional sobre el tipo de sangre
}

# Acceder al valor asociado con la clave "ciudad" y modificarlo
informacion_personal["ciudad"] = "Quito"  # Modificando la ciudad a "Quito"

# Verificar si la clave "telefono" existe en el diccionario
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "+593962014679"  # Agregando el número de teléfono ficticio

# Eliminar la clave "edad" del diccionario
del informacion_personal["edad"]

# Imprimir el diccionario final después de todas las operaciones
print("Diccionario final:", informacion_personal)
