def MinDivisor(n):
    i = 1
    divider = 1
    while i <= n**0.5:
        if n % i == 0 and n // i < n:
            divider = i
            break
        else:
            divider = n
        i += 1
    return divider


n = int(input())
print(MinDivisor(n))
