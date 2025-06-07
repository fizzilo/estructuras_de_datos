# Counting Sort

## 📌 Descripción
Counting Sort usa un arreglo auxiliar para contar la cantidad de ocurrencias de cada elemento.

## ⚙️ Funcionamiento
1. Calcula la frecuencia de cada número.
2. Usa esta información para reconstruir la lista ordenada.

## 🖥️ Código en Python
```python
def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    
    for num in arr:
        count[num] += 1
    
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])
    return sorted_arr
