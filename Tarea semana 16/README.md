Explicación:
Escritura de Archivo de Texto:

Usamos open() en modo "w" para abrir o crear el archivo my_notes.txt.
Usamos write() para escribir tres líneas en el archivo.
Lectura de Archivo de Texto:

Usamos open() en modo "r" para abrir el archivo.
Leemos cada línea del archivo utilizando un bucle for y mostramos cada línea en la consola.
Cierre de Archivos:

Utilizamos el bloque with, lo que asegura que el archivo se cierre automáticamente al final de cada operación, tanto para lectura como para escritura.