def quicksort(arr, left, right):

    if left < right:
        print(arr[left:right])

        pi = partition(arr, left, right)

        quicksort(arr, left, pi - 1)
        quicksort(arr, pi + 1, right)

    return arr


def partition(arr, left, right):
    sub = arr[left:right]
    pivot = arr[right]

    i = left - 1

    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1


# arr = [0, 3, 6, 23, 2, 5, 1]
arr = [0, 3, 6, 7, 8, 4, 2, 1, 5]


print('Unsorted array:', arr)
sorted_arr = quicksort(arr, 0, len(arr) - 1)
print('Sorted array:', sorted_arr)
