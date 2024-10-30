def merge(arr,i,m,r):
    n1=m-i+1
    n2=r-m
    L=[0]*n1
    R=[0]*n2
    for x in range(n1):
        L[x]=arr[i+x]
    for y in range(0,n2):
        R[y]=arr[m+1+y]
    x=0
    y=0
    k=i
    while x<n1 and y<n2:
        if L[x]<=R[y]:
            arr[k]=L[x]
            x+=1
        else:
            arr[k]=R[y]
            y+=1
        k+=1
    while x<n1:
        arr[k] = L[x]
        x+=1
        k+=1
    while y<n2:
        arr[k]=R[y]
        y+=1
        k+=1

def mergesort(arr, i, r):
    if i<r:
        m = i+(r-i)//2
        mergesort(arr,i,m)
        mergesort(arr,m+1,r)
        merge(arr,i,m,r)
        
    

arr=[12,11,13,5,6,7]
n=len(arr)
print("given array is: ")
for i in range(n):
    print("%d"%arr[i])
    
mergesort(arr, 0, n-1)
print("\nsorted array is")
for i in range(n):
    print("%d"%arr[i])




#gpt code
        
def merge(arr, i, m, r):
    n1 = m - i + 1
    n2 = r - m
    L = [0] * n1
    R = [0] * n2

    for x in range(0, n1):
        L[x] = arr[i + x]
    for y in range(0, n2):
        R[y] = arr[m + 1 + y]
    
    # Merge the temp arrays back into arr[i..r]
    x = 0
    y = 0
    k = i
    while x < n1 and y < n2:
        if L[x] <= R[y]:
            arr[k] = L[x]
            x += 1
        else:
            arr[k] = R[y]
            y += 1
        k += 1
    
    # Copy remaining elements of L[], if any
    while x < n1:
        arr[k] = L[x]
        x += 1
        k += 1
    
    # Copy remaining elements of R[], if any
    while y < n2:
        arr[k] = R[y]
        y += 1
        k += 1

def mergesort(arr, i, r):
    if i < r:
        m = i + (r - i) // 2
        mergesort(arr, i, m)
        mergesort(arr, m + 1, r)
        merge(arr, i, m, r)

# Test the corrected code
arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
print("Given array is: ")
for i in range(n):
    print("%d" % arr[i], end=" ")

mergesort(arr, 0, n - 1)
print("\nSorted array is: ")
for i in range(n):
    print("%d" % arr[i], end=" ")
        
        
