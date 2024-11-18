def selection_sort(arr):
    n = len(arr)
    
    # Select every element one by one and compare with the rest of the array - line 12
    for i in range(n - 1):
        min_idx = i
        
        # Iterate in the unsorted portion of the array until you find the minimum
        for j in range(i + 1, n):
            
            # Compare the selected element with the element selected from the unsorted portion
            if arr[j] < arr[min_idx]:
                
                # Set the min_idx to the index of the smallest element you find when iterating
                min_idx = j
        
        # Swap the current element and the minimum element
        print(f"ITERATION {i + 1}")
        print(f"Swapping elements: {arr[i]} and {arr[min_idx]}")
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(f"Array after swap: {arr}")
        
def print_array(arr):
    for val in arr:
        print(val, end=" ")
    print()

if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    
    print("Original array: ", end="")
    print_array(arr)
    
    selection_sort(arr)
    
    print("Sorted array: ", end="")
    print_array(arr)