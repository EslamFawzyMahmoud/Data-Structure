def linearsearch(arr,n,x):

    for i in range(n):
        if arr[i] == x:
            return i

    return -1

arr = [2, 3, 4, 10, 40]
x = 4

print(linearsearch(arr,len(arr)-1,x))