# Memoization in Python

## Explicit Memoization
```python
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
```

## Memoization with functools.lru_cache
```python
@lru_cache(maxsize=1000)
def fibonacci_3(n):
    if n < 1:
        return 0
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci_3(n - 1) + fibonacci_3(n - 2)
```