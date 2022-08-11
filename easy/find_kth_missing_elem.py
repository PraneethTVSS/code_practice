"""
Find the Kth missing element in a
Sorted array
"""
def find_kth_missing_elem(arr, n, k):

    start = arr[0]
    iter_range = n + k
    for idx in range(iter_range):
        if start in arr:
            start += 1
            continue

        missing_elem = start
        k -= 1
        if not k:
            return missing_elem
        
print(find_kth_missing_elem([1, 3, 5, 7, 9], 5, 1))
print(find_kth_missing_elem([3, 4, 5, 6], 4, 6))
