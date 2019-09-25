# Memoization in Python
> Created by Nicholas Ramsay

## Explicit Memoization
```python
fibonacci_cache = {}

def fibonacci(n):

    # Check if in cache
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    # Compute regular fibonacci
    if n < 1:
        result = 0
    if n == 1 or n == 2:
        result = 1
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)

    # Store value in cache and return value
    fibonacci_cache[n] = result
    return result
```

## Memoization with functools.lru_cache
```python
from functools import lru_cache

@lru_cache(maxsize=1000)
def fibonacci(n):
    if n < 1:
        return 0
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
```