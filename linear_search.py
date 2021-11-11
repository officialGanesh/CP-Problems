

def linearSearch(arr,key):
    """Finding key in array using linear search"""

    count = 0

    for i in range(len(arr)):
        if(key==arr[i]):
            print(f"Key ({key}) is present at index {i}")
            count += 1
    print(f"({key}) occured {count} times in {arr} 🚀")


print(linearSearch([10,290,90,89],89))