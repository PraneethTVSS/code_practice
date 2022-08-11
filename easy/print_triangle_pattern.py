"""
Print Triangle pattern
    *
   * * *
 * * * * *
"""
def print_pattern(n):
    
    for i in range(1, n+1):
        
        for spaces in range(n-i):
            print(" ", end="")
            
        for star in range(2*i - 1):
            print('*', end="")
            

print(print_pattern(4))
print(print_pattern(8))
