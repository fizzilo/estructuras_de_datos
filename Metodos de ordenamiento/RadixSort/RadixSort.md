# Radix Sort

## 📌 Descripción
Radix Sort es un algoritmo de ordenamiento que organiza los números considerando sus dígitos, desde el menos significativo hasta el más significativo.

## ⚙️ Funcionamiento
1. Encuentra el número más grande para determinar la cantidad de dígitos.
2. Ordena los números según cada dígito usando Counting Sort.
3. Repite el proceso para cada posición decimal hasta que todos los números estén ordenados.

## 🖥️ Código en Python
```python
def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10
    return arr
