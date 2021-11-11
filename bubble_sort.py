

def bubbleSort(arr):
    """Sort an array using bubble sort"""

    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]

    return arr

print(bubbleSort([10,8,-1,-8,0,19,90,77,-789876]))

