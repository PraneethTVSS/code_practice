"""
Nth Fibanocii number
"""

def fib(n):
    
    if n in [1, 2]:
        return 1
    
    return fib(n-1) + fib(n-2)

print(fib(4))
print(fib(5))
print(fib(7))
