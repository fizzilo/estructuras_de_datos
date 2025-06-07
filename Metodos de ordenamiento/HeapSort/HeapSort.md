# Heap Sort

## 📌 Descripción
Heap Sort usa una estructura de datos llamada heap para organizar los elementos de manera eficiente.

## ⚙️ Funcionamiento
1. Convierte la lista en un heap.
2. Extrae el elemento máximo y lo coloca en su posición final.
3. Reajusta el heap y repite el proceso.

## 🖥️ Código en Python
```python
import heapq

def heap_sort(arr):
    heapq.heapify(arr)
    sorted_arr = [heapq.heappop(arr) for _ in range(len(arr))]
    return sorted_arr
