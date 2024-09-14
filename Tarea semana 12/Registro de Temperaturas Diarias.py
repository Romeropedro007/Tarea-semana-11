# Datos: Matriz 3D (Ciudades, Días de la semana, Semanas)
# 3 ciudades, 7 días de la semana, 2 semanas (puedes agregar más semanas o ciudades si es necesario)
temperaturas = [
    [  # Ciudad 1
        [20, 22, 21, 19, 23, 25, 24],  # Semana 1
        [21, 23, 22, 20, 24, 26, 25]  # Semana 2
    ],
    [  # Ciudad 2
        [15, 17, 18, 16, 19, 20, 21],  # Semana 1
        [16, 18, 19, 17, 20, 21, 22]  # Semana 2
    ],
    [  # Ciudad 3
        [30, 32, 31, 29, 33, 35, 34],  # Semana 1
        [31, 33, 32, 30, 34, 36, 35]  # Semana 2
    ]
]

# Nombres de las ciudades
ciudades = ["Ciudad 1", "Ciudad 2", "Ciudad 3"]

# Iterar sobre cada ciudad
for i, ciudad in enumerate(temperaturas):
    print(f"Promedio de temperaturas para {ciudades[i]}:")

    # Iterar sobre cada semana
    for semana, dias in enumerate(ciudad):
        promedio_semana = sum(dias) / len(dias)
        print(f"  Semana {semana + 1}: {promedio_semana:.2f}°C")

