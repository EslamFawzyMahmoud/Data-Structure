def Selectionsort(arr):

    for i in range(len(arr)):

        minval = i

        for j in range(i+1,len(arr)):

            if arr[minval] > arr[j]:

                minval = j

        temp=arr[i]

        arr[i]=arr[minval]

        arr[minval]=temp

    return arr

arr=[64 , 25 , 12 , 22 , 11]

print("Before Sort: ",arr)

print("After Sort: ",Selectionsort(arr))