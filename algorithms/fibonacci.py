def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

def fibonacci_fast(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    fibs = [0,1]
    for i in range(2, n + 1):
        el = fibs[-1] + fibs[-2]
        fibs.append(el)

    return fibs[-1]

print(fibonacci_fast(4))
