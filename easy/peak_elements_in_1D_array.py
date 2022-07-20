"""
Peak elements of 1D array
Peak elements of an array are the elements that are greater than their adjacent 
elements.
The adjacent elements of an element at index i are elements at index i-1, i+1.
For corner elements, we have only one adjacent element
"""

def peak_elements(arr):
    
    peak_elems_indices = set()
    for idx, elem in enumerate(arr):
        
        if not idx:
            if arr[idx] > arr[idx+1]:
                peak_elems_indices.append(idx)
                continue
        elif idx == len(arr) - 1:
            if arr[idx] > arr[idx-1]:
                peak_elems_indices.append(idx)
                continue
        else:
            if (arr[idx] > arr[idx+1]) and (arr[idx] > arr[idx-1]):
                peak_elems_indices.append(idx)
                continue

    return list(peak_elems_indices)

print(peak_elements([1, 2, -1, 3, 1, 10, 1]))
print(peak_elements([1, 2, 3, 5, 4]))
