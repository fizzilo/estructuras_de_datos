# Selection Sort

## 📌 Descripción
Selection Sort es un algoritmo de ordenamiento que busca el elemento más pequeño y lo coloca en la primera posición. Luego, repite este proceso con el resto de la lista.

## ⚙️ Funcionamiento
1. Encuentra el elemento más pequeño de la lista.
2. Intercambia ese elemento con el primero.
3. Repite el proceso con el resto de la lista hasta que esté ordenada.

## 🖥️ Código en Python
```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
