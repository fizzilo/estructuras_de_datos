def bucket_sort(arr):
    n = len(arr)
    bucket_count = 10  # Número de buckets
    buckets = [[] for _ in range(bucket_count)]

    max_val = max(arr)
    
    for num in arr:
        index = int(num * bucket_count / (max_val + 1))
        buckets[index].append(num)

    for bucket in buckets:
        bucket.sort()

    return [num for bucket in buckets for num in bucket]

# Ejemplo de uso
lista = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
print(bucket_sort(lista))
