def binarysearch(array, x, low, high):
    while low<=high:
        mid=low+(low)//2
        if array[mid]==x:
            return mid
        elif array[mid]<x:
            low=mid+1
        else:
            high=mid-1
        return -1
array=[3,4,5,6,8,7,9]

x=4
result=binarysearch(array,x,0,len(array)-1)
if result!=1:
    print("element is present at index"+str(result))
else:
    print("Not found")
