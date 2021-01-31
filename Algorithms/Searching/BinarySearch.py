def binarysearch(arr,l,r,x):
    if r>=l:
        mid = l+(r-1)// 2
        if arr[mid] == x:
            return mid
        elif arr[mid] >x:
            return binarysearch(arr,l,mid-1,x)
        else:
            return binarysearch(arr,mid+1,r,x)
    else:
        return -1

arr = [ 2, 3, 4, 10, 40 ]
x=10

print("Index = ",binarysearch(arr,0,len(arr)-1,x))
