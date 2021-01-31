def partiotion(arr,low,high):
    piovt = arr[high]
    i = low-1
    for j in range(low,high):
        if piovt >arr[j]:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]


    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


def Quicksort(arr,low,high):
    if low<high:
        po= partiotion(arr,low,high)
        Quicksort(arr,low,po-1)
        Quicksort(arr,po+1,high)

    return arr

arr = [10, 7, 8, 9, 1, 5]

n=len(arr)

print("Before Sort: ",arr)

print("After Sort: ",Quicksort(arr,0,n-1))