# Escritura en un archivo de texto

# Abre (o crea) el archivo my_notes.txt en modo de escritura ("w")
with open('my_notes.txt', 'w') as file:
    # Escribimos tres líneas de notas personales
    file.write("Primera nota: Aprender a manipular archivos en Python.\n")
    file.write("Segunda nota: La importancia de cerrar archivos correctamente.\n")
    file.write("Tercera nota: Subir mi código a GitHub.\n")

# Lectura del archivo de texto

# Abre el archivo my_notes.txt en modo de lectura ("r")
with open('my_notes.txt', 'r') as file:
    # Lee el contenido línea por línea
    for line in file:
        # Muestra cada línea en la consola
        print(line.strip())  # .strip() elimina los saltos de línea adicionales

# El archivo se cierra automáticamente al salir del bloque "with"
