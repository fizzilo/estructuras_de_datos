# Shell Sort

## 📌 Descripción
Shell Sort es una mejora de Insertion Sort que permite mover elementos grandes más rápido.

## ⚙️ Funcionamiento
1. Define un **gap** que separa elementos distantes.
2. Aplica Insertion Sort con estos elementos separados.
3. Reduce el **gap** y repite hasta que sea 1.

## 🖥️ Código en Python
```python
def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr
