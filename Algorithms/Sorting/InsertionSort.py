def Insertionsort(arr):

    for i in range(1,len(arr)):
        value = arr[i]
        j=i-1

        while value<arr[j] and j>=0:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = value
    return arr

arr = [12, 11, 13, 5, 6]


print("Before Sort: ",arr)

print("After Sort: ",Insertionsort(arr))