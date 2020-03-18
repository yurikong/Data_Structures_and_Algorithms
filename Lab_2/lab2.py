# 1.
def sqrt(N,left,right):
    if N<0:
        return -1
    if N==0 or N==1:
        return N
    if right-left==1:
        return right
    else:
        mid=(left+right)//2
        if mid**2==N:
            return mid
        elif mid**2>N:
            return sqrt(N,left,mid)
        else:
            return sqrt(N,mid,right)
N=int(input('Enter an integer: '))
print('ceiling of sqrt of N = ',sqrt(N,0,N))

# 2.
def k_split(a,left,right):
    if len(a)<2:
        return -1
    else:
        mid=(left+right)//2
        if a[mid]==1:
            if a[mid-1]==0:
                return mid
            else:
                return k_split(a,left,mid)
        else:
            return k_split(a,mid,right)
# Should request the user input!!
print('Enter the list: ')
a=[]
while(True):
    num = input()
    if num.isdigit():
        a.append(int(num))
    else:
        break
print(a)
print('K =',k_split(a,0,len(a)))
