"""
Find the minimum and maximum element
using Binary Search
"""
def find_max_min_elem(arr, low, high):

    if low < high:
        return str(arr[0]) + " " + str(arr[high])

    mid = (high + low) // 2

    if mid < len(arr) - 1 and arr[mid] > arr[mid+1]:
        return str(arr[mid+1]) + " " + str(arr[mid])

    elif arr[low] <= arr[mid]:
        return find_max_min_elem(arr, mid+1, high)

    else:
        return find_max_min_elem(arr, low, mid-1)

print(find_max_min_elem([4, 8, 9, 10], 0, 3))
print(find_max_min_elem([-10, -8, -5, -1, 5, 6], 0, 5))
