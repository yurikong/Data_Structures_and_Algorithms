import numpy as np

def partition(a, left, right):
    pivot = right
    right -= 1
    while left < right:
        while left <= right and a[left] <= a[pivot]:
            left += 1
        while left <= right and a[right] >= a[pivot]:
            right -= 1
        if left < right:
            a[left], a[right] = a[right], a[left]
    if left < pivot and a[left] > a[pivot]:
        a[left], a[pivot] = a[pivot], a[left]
    return left
#use median3 for better run time
def quick_select(a, left, right, k):
    if k > 0 and right - left + 1 >= k:
        pivot = partition(a, left, right)
        len_left = pivot - left     # length of left sub array = (pivot - 1) - left + 1
        if len_left + 1 == k:
            return a[pivot]
        elif len_left + 1 > k:
            return quick_select(a, left, pivot - 1, k)
        else:
            return quick_select(a, pivot + 1, right, k - len_left - 1) # k - (len_left + 1)
    return False

def k_select(a, left, right, k):
    if k > 0 and right - left + 1 >= k:
        pivot = partition(a, left, right)
        len_left = pivot - left     # length of left sub array = (pivot - 1) - left + 1
        if len_left + 1 == k:
            return pivot
        elif len_left + 1 > k:
            return k_select(a, left, pivot - 1, k)
        else:
            return k_select(a, pivot + 1, right, k - len_left - 1)
    return False

def max_k_numbers(a, left, right, k):
    n = len(a)
    if k == n:
        return a
    if k > 0 and k <= n:
        x = n - k
        pivot = k_select(a, left, right, x)
        return a[pivot + 1:]
    return False

n = int(input('Enter a positive integer: '))
a = np.random.randint(-100, 101, n)
print(a)
msg = 'Enter a number between 1 to ' + str(n) + ': '
k = int(input(msg))
left = 0
right = len(a) - 1
b=a.copy()
print('the', k, '-th least element is ', quick_select(a, left, right, k))
print('the max', k, 'numbers of elements are\n', max_k_numbers(b, left, right, k))
