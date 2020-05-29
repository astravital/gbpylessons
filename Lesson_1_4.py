s = input('Vvedite celoe polojitelnoe chislo - ')
i = 0
max1 = 0
while i < len(s):
    if max1 < int(s[i]):
        max1 = int(s[i])
    i += 1
print('maximalnaya cifra vvedennogo chisla - ', max1)
