import numpy as np
import time
import math

def insertion_sort(a):
    n=len(a)
    for i in range(1,n):
        for j in range(i-1,-1,-1):
            if a[j+1]<a[j]:
                a[j+1],a[j]=a[j],a[j+1]
            else:
                break
    return a

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

n=int(input('Enter a positive integer: '))   # n=1000
num=100
iTotal=0
qTotal=0
for i in range(0,num):
    a=np.random.randint(-5000,5001,n)
    a_copy=a.copy()
    start=time.time()
    insertion_sort(a)
    iTotal+=time.time()-start
    start=time.time()
    quick_sort(a_copy,0,len(a_copy)-1)
    qTotal+=time.time()-start
iAvg=iTotal/num
qAvg=qTotal/num
iStep=iAvg/n**2
print('Total run time for insertion sort in',num,'times =',iTotal,'s')
print('Total run time for quick sort in',num,'times =',qTotal,'s')
print('Run time for a single run of insertion sort in',num,'times =',iStep,'s')
print('My machine can run',1/iStep,'insturctions in a second using insertion sort')
a = [4,6,3,2,6,7,9,3,10,95]
insertion_sort(a)
print(a)
