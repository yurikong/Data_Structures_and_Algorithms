def min_heapify(a, index, n):
    left = index * 2 + 1
    right = index * 2 + 2
    min = index
    if left < n and a[left] < a[min]:
        min = left
    if right < n and a[right] < a[min]:
        min = right
    if min != index:
        a[min], a[index] = a[index], a[min]
        min_heapify(a, min, n)
        
def build_MinHeap(a):
    n = len(a)
    start = n//2 - 1
    for i in range(start, -1, -1):
        min_heapify(a, i, n)

a1 = [0, 2, 4, 6]
a2 = [1, 5, 8, 10]
a3 = [3, 7, 9, 20]
n = len(a1)
