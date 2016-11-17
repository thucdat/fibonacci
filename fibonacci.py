def fibonacci(n):
    a = 0
    b = 1
    for i in range(0, n):
        temp = a
        a = b
        b = temp + b
    return a

def test_fibonacci(n):
    if n < 2:
        return fibonacci(n) == n
    return fibonacci(n+1) == fibonacci(n) + fibonacci(n-1)