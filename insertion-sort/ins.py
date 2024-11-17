def insertion_sort(arr):
    for i in range(1, len(arr)): #start from 2. element and go until the last one
        key = arr[i]
        j = i - 1 #mark the previous element
        
        while j >= 0 and key < arr[j]: #while the key is less than previous element, move 1 left (or more formally move the compared element one right)
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key #insert the key at the correct position, (+1) is because we incremented it to check if it is bigger than the key or not
        
# A utility function to print array of size n
def printArray(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

# Driver method
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    insertion_sort(arr)
    printArray(arr)