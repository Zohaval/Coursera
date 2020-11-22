word = input()
F = word.find('f')
R = word.rfind('f')
if F == -1:
    print()
elif F == R:
    print(F)
else:
    print(F, R)
