import numpy as np
import time

def max_heapify(a, index, n):
    left = index * 2 + 1
    right = index * 2 + 2
    max = index
    if left < n and a[left] > a[max]:
        max = left
    if right < n and a[right] > a[max]:
        max = right
    if max != index:
        a[max], a[index] = a[index], a[max]
        max_heapify(a, max, n)
        
def build_MaxHeap(a):
    n = len(a)
    start = n//2 - 1
    for i in range(start, -1, -1):
        max_heapify(a, i, n)

def heap_sort(a, n):
    build_MaxHeap(a)
    while n > 0:
        a[0], a[n-1] = a[n-1], a[0]
        max_heapify(a, 0, n - 1)
        n -= 1

def selection_sort(a, n):
    for i in range(0, n):
        min = i
        for j in range(i + 1, n):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]

# part A
n = int(input('Enter a positive integer: '))
lowerbound = -10000
upperbound = 10001
a = np.random.randint(lowerbound, upperbound, n)
heap_sort(a, n)
print('done')

##ntimes = 100
##heap_total = 0
##sel_total = 0
##for i in range(ntimes):
##    a = np.random.randint(lowerbound, upperbound, n)
##    heap_start = time.time()
##    heap_sort(a, n)
##    heap_total += time.time() - heap_start
##    
##for i in range(ntimes):
##    a = np.random.randint(lowerbound, upperbound, n)
##    sel_start = time.time()
##    selection_sort(a, n)
##    sel_total = time.time() - sel_start
##    
##heap_avg = heap_total / ntimes
###heap_step = heap_avg / (n * np.log2(n))
##sel_avg = sel_total / ntimes
###sel_step = sel_avg / (n**2)
##print('Average for heap sort for ', ntimes, ' times is ', heap_avg)
##print('Average for selection sort for ', ntimes, ' times is ', sel_avg)

ntimes = 1000
heap_total = 0
sel_total = 0
for i in range(ntimes):
    a = np.random.randint(lowerbound, upperbound, n)
    heap_start = time.time()
    heap_sort(a, n)
    heap_total += time.time() - heap_start

for i in range(ntimes):
    a = np.random.randint(lowerbound, upperbound, n)
    sel_start = time.time()
    selection_sort(a, n)
    sel_total = time.time() - sel_start
    
heap_avg = heap_total / ntimes
#heap_step = heap_avg / (n * np.log2(n))
sel_avg = sel_total / ntimes
#sel_step = sel_avg / (n**2)
print('Average for heap sort for ', ntimes, ' times is ', heap_avg)
print('Average for selection sort for ', ntimes, ' times is ', sel_avg)

# part B
n = 10
arr = np.random.randint(-10, 11, n)
print(arr)
heap_sort(arr, n)
print(arr)
