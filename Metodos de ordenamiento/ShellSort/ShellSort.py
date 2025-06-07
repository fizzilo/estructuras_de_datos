def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # Inicializa el espacio entre elementos

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2  # Reduce el espacio entre elementos
    return arr

# Ejemplo de uso
lista = [64, 25, 12, 22, 11]
print(shell_sort(lista))
