import random

def partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]
    
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    
    return i + 1

def paranoid_quicksort(arr, low, high):
    while low < high:
        pivot_index = partition(arr, low, high)
        
        # Check if the pivot is a good pivot
        if pivot_index - low <= (3/4) * (high - low) and high - pivot_index <= (3/4) * (high - low):
            paranoid_quicksort(arr, low, pivot_index - 1)
            low = pivot_index + 1
        else:
            # Repeat the process with a new random pivot
            pivot_index = random.randint(low, high)
            arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    
    # Final sorting to handle small partitions
    for i in range(low, high + 1):
        for j in range(i, low, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break

# Example usage:
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
paranoid_quicksort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
