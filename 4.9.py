def ReduceFraction(n, m):
    if n != 0 and m != 0:
        if n > m:
            n = n % m
        else:
            m = m % n
    elif n > m:
        return n
    else:
        return m
    return ReduceFraction(n, m)


n = int(input())
m = int(input())
print(n // ReduceFraction(n, m), m // ReduceFraction(n, m))
