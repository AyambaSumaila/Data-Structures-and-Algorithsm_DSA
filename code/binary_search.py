def binary_search(arr, low, high, key):
    #if low == high, it means the array does not contain any element
    
    while low <= high: 
        mid =int(low + (high - low)/2)
        if arr[mid] == key: 
            return mid 
        elif arr[mid] < key:
            low= mid + 1
        else: 
            high = mid + 1
            
    return -1


#Test it with some input 
arr=[23, 45, 63, 90, 100]
a=90

result= binary_search(arr, 0, len(arr)-1, a)
print(result)