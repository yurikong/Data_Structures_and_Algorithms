import numpy as np

def MSS_n(a):
    MSS = 0
    sum = 0
    for i in range(len(a)):
        sum += a[i]
        if sum < 0:
            sum = 0
        if sum > MSS:
            MSS = sum
    return MSS

def cross_sum(a, left, right):
    mid = (left + right)//2
    left_sum = 0
    left_mss = 0
    right_sum = 0
    right_mss = 0
    for i in range(mid, left - 1, -1):
        left_sum += a[i]
        if left_sum > left_mss:
            left_mss = left_sum
    for i in range(mid + 1, right + 1):
        right_sum += a[i]
        if right_sum > right_mss:
            right_mss = right_sum
    return left_mss + right_mss

def MSS_nlogn(a, left, right):
    if left == right:
        return a[left]
    mid = (left + right)//2
    return max(MSS_nlogn(a, left, mid), MSS_nlogn(a, mid + 1, right), cross_sum(a, left, right))

n = int(input('Enter a positive integer: '))
a = np.random.randint(-100, 101, n)
print(a)
print(MSS_n(a))
print(MSS_nlogn(a, 0, len(a) - 1))
