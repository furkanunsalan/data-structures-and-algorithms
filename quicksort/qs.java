import java.util.Arrays;

public class QuickSort {
    
    public static void quicksort(int[] arr, int low, int high) {
        if (low < high) {
            int pi = partition(arr, low, high);
            quicksort(arr, low, pi - 1);  // Recursively sort the left partition
            quicksort(arr, pi + 1, high); // Recursively sort the right partition
        }
    }

    private static int partition(int[] arr, int low, int high) {
        int pivot = arr[high];  // Select the pivot (last element)
        int i = (low - 1);  // Index of the smaller element
        
        for (int j = low; j < high; j++) {
            if (arr[j] < pivot) {
                i++;
                // Swap arr[i] and arr[j]
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
        
        // Swap arr[i+1] and arr[high] (or pivot)
        int temp = arr[i + 1];
        arr[i + 1] = arr[high];
        arr[high] = temp;

        return i + 1;  // Return the partitioning index
    }

    public static void main(String[] args) {
        int[] arr = {10, 7, 8, 9, 1, 5};
        int n = arr.length;
        
        quicksort(arr, 0, n - 1);
        
        System.out.println("Sorted array: " + Arrays.toString(arr));
    }
}

