# Matriz 3x3 con valores numéricos
matriz = [
    [9, 4, 6],
    [2, 8, 1],
    [5, 3, 7]
]

def bubble_sort_fila(matriz, fila):
    n = len(matriz[fila])
    for i in range(n):
        for j in range(0, n-i-1):
            if matriz[fila][j] > matriz[fila][j+1]:
                matriz[fila][j], matriz[fila][j+1] = matriz[fila][j+1], matriz[fila][j]

# Mostrar matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Ordenar la segunda fila (índice 1)
bubble_sort_fila(matriz, 1)

# Mostrar matriz con la fila ordenada
print("\nMatriz con la segunda fila ordenada:")
for fila in matriz:
    print(fila)
