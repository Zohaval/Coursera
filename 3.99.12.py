string = input()
i = string.find('f')
string_2 = string[i + 1::]
i_2 = string_2.find('f')
if i_2 == -1:
    if i != -1:
        print(-1)
    else:
        print(-2)
else:
    print(i_2 + i + 1)
