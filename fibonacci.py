def fib(n):
    a = 0
    b = 1
    for i in range(1,n+1):
            c = a + b
            #print c
            a = b
            b = c
    return c

def test_fib(n):
    return fib(n + 1) == fib(n) + fib(n - 1)