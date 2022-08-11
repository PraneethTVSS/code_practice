"""
N ladders positioned in straight line, special ladder means
if all the ladders towards are higher than the current ladder
and the rightmost is always the special ladder
"""
def special_ladders(arr):
    
    prev_ladder = arr[-1]
    count = 1 # Since the rightmost ladder is always a special
    for ladder in arr[-2::-1]: # Iterating from the 2nd last element
        
        if ladder < prev_ladder:
            prev_ladder = ladder
            count += 1

    return count

print(special_ladders([4, 5, 1, 3, 2])) # output: 3
print(special_ladders([9, 8, 10, 12])) # output: 1
