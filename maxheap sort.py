def heapify(arr, n, i):
    """
    Maintains the max heap property for a subtree rooted at index `i`.
    `n` is the active heap size.
    """
    largest = i          # Initialize largest as root
    left = 2 * i + 1     # Left child index
    right = 2 * i + 2    # Right child index

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        
        heapify(arr, i, 0)

    return arr

if __name__ == "__main__":
    raw_input = input("Enter numbers separated by spaces: ")
    
    user_array = [int(x) for x in raw_input.split()]
    
    print("\nOriginal array:", user_array)
    
    sorted_array = heap_sort(user_array)
    
    print("Sorted array (Ascending):", sorted_array)
