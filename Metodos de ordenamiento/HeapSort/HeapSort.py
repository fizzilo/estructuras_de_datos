import heapq

def heap_sort(arr):
    heapq.heapify(arr)  # Convierte la lista en un heap
    sorted_arr = [heapq.heappop(arr) for _ in range(len(arr))]
    return sorted_arr

# Ejemplo de uso
lista = [10, 3, 5, 8, 2, 7, 4]
print(heap_sort(lista))
