# This implementation uses list compreension in order to find the subarrays in the left or right from pivot

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        bigger_than_pivot = [x for x in arr[1:] if x > pivot]

        return quicksort(less_than_pivot) + [pivot] + quicksort(bigger_than_pivot)


# arr = [0, 3, 6, 23, 2, 5, 1]
arr = [0, 3, 6, 7, 8, 4, 2, 1, 5]


print('Unsorted array:', arr)
sorted_arr = quicksort(arr)
print('Sorted array:', sorted_arr)
