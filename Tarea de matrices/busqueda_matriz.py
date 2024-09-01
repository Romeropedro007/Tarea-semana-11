# Matriz 3x3 con valores numéricos
matriz = [
    [5, 8, 10],
    [3, 7, 1],
    [9, 6, 4]
]

def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return f"Valor {valor} encontrado en la posición ({i}, {j})"
    return f"Valor {valor} no encontrado en la matriz."

# Pedir al usuario que ingrese el valor a buscar
valor_buscado = int(input("Introduce el valor que deseas buscar en la matriz: "))

# Buscar el valor en la matriz y mostrar el resultado
resultado = buscar_valor(matriz, valor_buscado)
print(resultado)
