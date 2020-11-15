P = int(input())
X = int(input())
Y = int(input())
Y = Y / 100
S = X + Y
P = 1 + P/100
S *= P
s = S * 100
print(int(S), int(s % 100))
