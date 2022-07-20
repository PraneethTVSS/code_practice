"""
Find the element in 1D array
"""

def binary_search(arr, high, low, k):
    
    mid = (high + low) // 2
    
    if high < low:
        return -1
    
    if arr[mid] == k:
        return mid
    elif arr[mid] > k:
        return binary_search(arr, low, mid-1, k)
    else:
        return binary_search(arr, mid+1, low, k)
    
print(binary_search([4, 8, 9, 10], 0, 4, 9))
print(binary_search([-10, -8, -5, -1, 5, 6], 0, 6, -1))
