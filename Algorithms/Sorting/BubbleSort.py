def bubblesort(arr):

    for i in range(len(arr)-1):

        for j in range(len(arr)-1):

            if arr[j] > arr[j+1]:

                temp = arr[j]

                arr[j] = arr[j+1]

                arr[j+1] = temp
    return arr

arr=[5,4,1,2,7,8,0,100,6]

print("Before Sort: ",arr)

print("After Sort: ",bubblesort(arr))