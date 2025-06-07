# Bubble Sort

## 📌 Descripción
Bubble Sort es un algoritmo de ordenamiento que compara elementos adyacentes y los intercambia si están en el orden incorrecto. Repite este proceso hasta que toda la lista esté ordenada.

## ⚙️ Funcionamiento
1. Se recorren los elementos del array varias veces.
2. Se comparan elementos consecutivos.
3. Si el elemento actual es mayor que el siguiente, se intercambian.
4. Se repite hasta que la lista está completamente ordenada.

## 🖥️ Código en Python
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Ejemplo de uso
lista = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(lista))
