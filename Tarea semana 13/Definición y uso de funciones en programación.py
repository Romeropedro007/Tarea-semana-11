# Definimos la función para calcular el promedio de temperaturas
def calcular_promedio_temperaturas(temperaturas, ciudades):
    """
    Esta función calcula y muestra el promedio de temperaturas para cada ciudad
    durante cada semana.

    Parámetros:
    - temperaturas: lista 3D con las temperaturas de varias ciudades por semana y día.
    - ciudades: lista con los nombres de las ciudades.
    """

    for i, ciudad in enumerate(temperaturas):
        print(f"Promedio de temperaturas para {ciudades[i]}:")

        # Iteramos sobre cada semana
        for semana, dias in enumerate(ciudad):
            promedio_semana = sum(dias) / len(dias)
            print(f"  Semana {semana + 1}: {promedio_semana:.2f}°C")


# Ejemplo de uso con 3 ciudades, 7 días de la semana, y 4 semanas
temperaturas = [
    [  # Ciudad 1
        [20, 22, 21, 19, 23, 25, 24],  # Semana 1
        [21, 23, 22, 20, 24, 26, 25],  # Semana 2
        [22, 24, 23, 21, 25, 27, 26],  # Semana 3
        [23, 25, 24, 22, 26, 28, 27]  # Semana 4
    ],
    [  # Ciudad 2
        [15, 17, 18, 16, 19, 20, 21],  # Semana 1
        [16, 18, 19, 17, 20, 21, 22],  # Semana 2
        [17, 19, 20, 18, 21, 22, 23],  # Semana 3
        [18, 20, 21, 19, 22, 23, 24]  # Semana 4
    ],
    [  # Ciudad 3
        [30, 32, 31, 29, 33, 35, 34],  # Semana 1
        [31, 33, 32, 30, 34, 36, 35],  # Semana 2
        [32, 34, 33, 31, 35, 37, 36],  # Semana 3
        [33, 35, 34, 32, 36, 38, 37]  # Semana 4
    ]
]

ciudades = ["Ciudad 1", "Ciudad 2", "Ciudad 3"]

# Llamamos a la función
calcular_promedio_temperaturas(temperaturas, ciudades)
