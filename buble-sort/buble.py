def bubbleSort(arr):
    n = len(arr)
    print(f"Initial Array: {arr}")
    
    # Traverse every element of the array
    for i in range(n):
        # Track if the element is already swapped
        swapped = False
        
        # Last "i" elements are already in sorted order so skip them by reducing it from the end
        for j in range(0, n - i - 1):
            
            # Check if the next element is bigger than our current element
            if arr[j] > arr[j + 1]:
                
                # Swap the elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # Change the flag
                swapped = True
        
        print(f"Array after the iteration {i}: {arr}")
        
        if swapped == False:
            break

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]

    bubbleSort(arr)

    print("Sorted array:")
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")