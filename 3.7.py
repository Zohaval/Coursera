from math import sqrt
a = float(input())
b = float(input())
c = float(input())
D = b*b - 4*a*c
if D > 0:
    x1 = (-b + sqrt(D)) / (2*a)
    x2 = (-b - sqrt(D)) / (2*a)
    if x1 > x2:
        print('{0:.7f}'.format(x2), '{0:.7f}'.format(x1))
    else:
        print('{0:.7f}'.format(x1), '{0:.7f}'.format(x2))
elif D == 0:
    x = -b / (2*a)
    print('{0:.7f}'.format(x))
