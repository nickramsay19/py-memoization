from functools import lru_cache

'''
    --- Regualar Fibonacci ---
'''
def fibonacci_1(n):
    if n < 1:
        return 0
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci_1(n - 1) + fibonacci_1(n - 2)

'''
    --- Explicit Fibonacci ---
'''
fibonacci_cache = {}

def fibonacci_2(n):

    # Check if in cache
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    # Compute regular fibonacci
    if n < 1:
        result = 0
    if n == 1 or n == 2:
        result = 1
    else:
        result = fibonacci_2(n - 1) + fibonacci_2(n - 2)

    # Store value in cache and return value
    fibonacci_cache[n] = result
    return result

'''
    --- lru_cache Fibonacci ---
'''
@lru_cache(maxsize=1000)
def fibonacci_3(n):
    if n < 1:
        return 0
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci_3(n - 1) + fibonacci_3(n - 2)

'''
    --- Showcase ---
'''
for n in range(1,1000):
    print(str(n) + ' : ' + str(fibonacci_3(n)))
