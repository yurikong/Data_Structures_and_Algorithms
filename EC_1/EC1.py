# 1.
def medianOf2(a,b,n):
    if n==0:
        return -1
    elif n==1:
        return (a[0]+b[0])/2
    elif n==2:
        return (max(a[0],b[0])+min(a[1],b[1]))/2
    else:
        if n%2==0:
            m1=(a[n//2-1]+a[n//2])/2
            m2=(b[n//2-1]+b[n//2])/2
        else:
            m1=a[n//2]
            m2=b[n//2]
        if m1<m2:
            if n%2==0:
                return medianOf2(a[n//2-1:],b[:n//2+1],n//2+1)
            else:
                return medianOf2(a[n//2:],b[:n//2+1],n//2+1)
        else:
            if n%2==0:
                return medianOf2(a[:n//2+1],b[n//2-1:],n//2+1)
            else:
                return medianOf2(a[:n//2+1],b[n//2:],n//2+1)
a=[0,2,10,26,68]
b=[1,11,18,20,41]
n=len(a)
print('Median =',medianOf2(a,b,n))
a=[5,6,14,26]
b=[3,41,88,100]
print('Median =',medianOf2(a,b,n))
a=[5,10]
b=[2,41]
print('Median =',medianOf2(a,b,n))
# 2.
def findFirstMissing(a,left,right,n):
    if left>right:
        return n
    if a[left]!=left:
        return left
    mid=(left+right)//2
    if a[mid]==mid:
        return findFirstMissing(a,mid+1,right,n)
    return findFirstMissing(a,left,mid,n)
a=[0,1,3,8,9]
n=len(a)
print(findFirstMissing(a,0,n-1,n))
a=[2,5,7,11]
print(findFirstMissing(a,0,n-1,n))
a=[0,1,2,3,4]
print(findFirstMissing(a,0,n-1,n))
a=[12]
print(findFirstMissing(a,0,n-1,n))
