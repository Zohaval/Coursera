def summa(a):
    a = int(input())
    if a == 0:
        return 0
    return a + summa(a)


a = 0
print(summa(a))
