def iterative_binary_search(arr, target):
    low = 0
    high = len(arr) - 1 # index of the last element
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid # found the target value
        elif arr[mid] < target:
            low = mid + 1
        else: # arr[mid] > target
            high = mid -1
    
    return -1 # no target found

arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 7

# Using iterative method
index_iterative = iterative_binary_search(arr, target)
print(f"Element found at index: {index_iterative}")