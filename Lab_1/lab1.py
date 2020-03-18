import numpy as np
import time
import math
# implementation of linearSearch(a,key)
def linearSearch(a,key):
    for i in a:
        if i==key:
            return True
    return False
# implementation of binarySearch(a,key)
def binarySearch(a,key):
    if len(a)==0:
        return False
    else:
        mid=len(a)//2
        if a[mid]==key:
            return True
        elif a[mid]<key:
            return binarySearch(a[mid+1:],key)
        else:
            return binarySearch(a[:mid],key)
# Part A. average-case running time
n=int(input('Enter a positive integer: ')) # n=10**5
a=np.random.randint(-1000,1001,n)
np.sort(a)
linear_total=0
numberOfTimes=100
for i in range(0,numberOfTimes):
    key=a[np.random.randint(n)]
    linear_start=time.time()
    linearSearch(a,key)
    linear_total+=time.time()-linear_start
linear_average=linear_total/numberOfTimes
binary_total=0
for i in range(0,numberOfTimes):
    key=a[np.random.randint(n)]
    binary_start=time.time()
    binarySearch(a,key)
    binary_total+=time.time()-binary_start
binary_average=binary_total/numberOfTimes
print('Average run time for linear search with n=',n,': ',linear_average,'s')
print('Average run time for binary search with n=',n,': ',binary_average,'s')
# Part B. worst-case running time
n=int(input('Enter a positive integer: ')) # n=10**5
a=np.random.randint(-1000,1001,n)
np.sort(a)
key=5000
start=time.time()
linearSearch(a,key)
runtime=time.time()-start
linearStepTime=runtime/n
start=time.time()
binarySearch(a,key)
runtime=time.time()-start
binaryStepTime=runtime/math.log2(n)                #Trung: runtime/log2(n)
print('Time needed to run a single step with linear search with n=',n,': ',linearStepTime,'s')
print('Time needed to run a single step with binary search with n=',n,': ',binaryStepTime,'s')
n=10**7
linearSearchTime=linearStepTime*n
binarySearchTime=binaryStepTime*math.log2(n)       #Khang: binaryStep*log2(n)
print('Calculation for worst case run time for linear search with n=',n,': ',linearSearchTime,'s')
print('Calculation for worst case run time for binary search with n=',n,': ',binarySearchTime,'s')
