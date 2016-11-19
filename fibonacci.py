# This is the simplest and fastest implementation of the fibonacci sequence in Python.
def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        temp = a
        a = b
        b = temp + b
    return a

# This is the test of the fibonacci sequence
# This test verifies:
# The fibonacci is the series of the numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# The first number is 0
# The second number is 1
# The next number is found by adding up the two numbers before it.
def test_fibonacci(n):
    if n < 2:
        return fibonacci(n) == n
    return fibonacci(n+1) == fibonacci(n) + fibonacci(n-1)
