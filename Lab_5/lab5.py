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

def quick_select(a, left, right, k):
    if k > 0 and right - left + 1 >= k:
        pivot = partition(a, left, right)
        len_left = pivot - left     # length of left sub array = (pivot - 1) - left + 1
        if len_left + 1 == k:
            return a[pivot]
        elif len_left + 1 > k:
            return quick_select(a, left, pivot - 1, k)
        else:
            return quick_select(a, pivot + 1, right, k - len_left - 1)
    return False

def k_closest_to_median(a, k):
    if k <= 0:
        return False
    if n < k + 1:
        return None
    if n % 2 == 0:
        mid = n // 2        # index = n//2 - 1, position = index + 1
    else:
        mid = n // 2 + 1    # index = n//2, position = index + 1
    median = quick_select(a, 0, n - 1, mid)
    diff = np.abs(a - median)
    diff = list(zip(diff, a))
    quick_select(diff, 0, n - 1, k + 1)
    result = []
    for i in range(k + 1):
        num = diff[i][1]
        if num != median:
            result.append(num)
    return result
# Trung: The requirement asks u to shift back the original values using mean.
# Using zip is illegal!
n = int(input('Enter a positive integer: '))
a = np.random.randint(-100, 101, n)
print(a)
K = int(input('Enter a number between 1 to ' + str(n) + ': '))
result = k_closest_to_median(a, K)
print(K, ' elements closest to the median = ', result)
