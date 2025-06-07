
# Tim Sort

## 📌 Descripción
Tim Sort es un algoritmo híbrido que combina **Merge Sort** e **Insertion Sort**, optimizado para listas reales en Python.

## ⚙️ Funcionamiento
1. Divide la lista en segmentos pequeños (runs).
2. Aplica **Insertion Sort** en cada segmento.
3. Usa **Merge Sort** para combinar los segmentos ordenados.

## 🖥️ Código en Python
```python
def tim_sort(arr):
    return sorted(arr)  # Python ya optimiza con Tim Sort
