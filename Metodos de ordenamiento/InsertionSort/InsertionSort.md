
# Insertion Sort

## 📌 Descripción
Insertion Sort construye una lista ordenada insertando un elemento a la vez en su posición correcta.

## ⚙️ Funcionamiento
1. Comienza con una lista ordenada de un solo elemento.
2. Toma el siguiente elemento y lo inserta en la posición correcta dentro de la lista ordenada.
3. Repite el proceso hasta que todos los elementos estén ordenados.

## 🖥️ Código en Python
```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
