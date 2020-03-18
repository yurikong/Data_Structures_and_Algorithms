import numpy as np
import sys

def median_of_three(a,left,right):
    mid=(left+right)//2
    if a[left]>a[mid]:
        a[left],a[mid]=a[mid],a[left]
    if a[left]>a[right]:
        a[left],a[right]=a[right],a[left]
    if a[mid]>a[right]:
        a[mid],a[right]=a[right],a[mid]
    return mid
    
def partition(a,left,right):
    pivot=median_of_three(a,left,right)
    a[pivot],a[right]=a[right],a[pivot]
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

def quick_sort(a,left,right):
    size=right-left+1
    if size<=1:
        return
    elif size==2:
        if a[left]>a[right]:
            a[left],a[right]=a[right],a[left]
    elif size==3:
        median_of_three(a,left,right)
    else:
        pivot=partition(a,left,right)
        quick_sort(a,left,pivot-1)
        quick_sort(a,pivot+1,right)

def MPSS_middle(a):
    #print('a:',a)
    n = len(a)
    mid = n//2
    left = a[:mid]
    right = a[mid:]
    #print('left:',left)
    #print('right:',right)
    leftSize = len(left)
    rightSize = len(right)
    leftsum = [0] * leftSize
    rightsum = [0] * rightSize
    sum = 0
    for i in range(leftSize - 1, -1, -1):
        sum += left[i]
        leftsum[i] = sum
    sum = 0
    for i in range(rightSize):
        sum += right[i]
        rightsum[i] = sum
    #print(leftsum)
    #print(rightsum)
    quick_sort(leftsum, 0, leftSize - 1)
    quick_sort(rightsum, 0, rightSize - 1)
    #print('leftsum:',leftsum)
    #print('rightsum:',rightsum)
    i = 0
    j = rightSize - 1
    min = sys.maxsize
    while i < leftSize and j > 0:
        s = leftsum[i] + rightsum[j]
        if s <= 0:
            i += 1
        elif s < min:
            min = s
        else:
            j -= 1
    #print('min middle:',min)
    return min
    
def MPSS(a):
    #print('a:',a)
    n = len(a)
    mid = n//2
    if n == 1:
        #print('min',a[0])
        if a[0] <= 0:
            return sys.maxsize
        else:
            return a[0]
    return min(MPSS(a[:mid]), MPSS(a[mid:]), MPSS_middle(a))

n = int(input('Enter an integer: '))
#a = [-34, 49, -58, 76, 29, -71, -54, 63]
#a = [2, -3, 1, 4, -6, 10, -12, 5.2, 3.6, -8]
a = np.random.uniform(-20, 21, n)
print(a)
#min = MPSS_middle(a)
print('MPSS:',MPSS(a))
