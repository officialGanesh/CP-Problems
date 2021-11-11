

def binarySearch(arr,key):
    """ Finding key in given array, sorted array must be passed"""
    left,right = 0,len(arr)-1

    
    while (left<=right):
        mid = int((left+right)/2)
        if(key==arr[mid]):
            return f"key ({key}) is present at index {mid}"
        elif(key<arr[mid]):
            right = mid - 1
        else:
            left = mid + 1

print(binarySearch([10,20,90,300],10))