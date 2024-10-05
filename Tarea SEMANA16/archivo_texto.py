# Escritura de Archivo de Texto
# Creamos un nuevo archivo llamado 'my_notes.txt' y escribimos algunas líneas

with open('my_notes.txt', 'w') as file:  # El modo 'w' crea el archivo si no existe
    file.write("Esta es mi primera línea de notas personales.\n")
    file.write("Aquí está la segunda línea, ¡a seguir aprendiendo!\n")
    file.write("Finalmente, la tercera línea para finalizar mis notas.\n")

# Lectura de Archivo de Texto
# Abrimos el archivo 'my_notes.txt' para leer su contenido línea por línea

with open('my_notes.txt', 'r') as file:  # El modo 'r' abre el archivo en modo lectura
    line = file.readline()  # Leer la primera línea
    while line:
        print(line, end='')  # Imprimir cada línea leída (end='' evita saltos de línea adicionales)
        line = file.readline()  # Leer la siguiente línea

# El archivo se cierra automáticamente al salir del bloque 'with'
