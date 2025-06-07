# Bucket Sort

## 📌 Descripción
Bucket Sort es un algoritmo que distribuye los elementos en diferentes contenedores (**buckets**) y los ordena individualmente.

## ⚙️ Funcionamiento
1. Se crean **buckets** y se asignan elementos a cada uno según su valor.
2. Se ordenan los elementos dentro de cada **bucket** usando otro algoritmo de ordenamiento.
3. Se combinan los **buckets** para obtener la lista ordenada.

## 🖥️ Código en Python
```python
def bucket_sort(arr):
    n = len(arr)
    bucket_count = 10
    buckets = [[] for _ in range(bucket_count)]
    max_val = max(arr)

    for num in arr:
        index = int(num * bucket_count / (max_val + 1))
        buckets[index].append(num)

    for bucket in buckets:
        bucket.sort()

    return [num for bucket in buckets for num in bucket]
