s = str(input())
orig = s.find(' ')
final = s[orig + 1:] + ' ' + s[:orig]
print(final)
