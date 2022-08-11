"""
Find the peak element in an array
"""

def peak_element(arr, low, high):

    if low >= high:
        return low
    
    mid = (low + high) // 2
    if arr[mid] > arr[mid+1]:
        return peak_element(arr, low, mid)
    else:
        return peak_element(arr, mid, high)
    
print(peak_element([1, 2, 3, 5, 3, 2], 0, 5))
print(peak_element([1, 4, 3, 2], 0, 3))
