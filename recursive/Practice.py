def fact(n, a = 1):
    if n == 0:
        return a
    else:
        return fact(n - 1, n * a)

print(fact(4,1))
