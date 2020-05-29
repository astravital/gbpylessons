a = int(input('a = '))
b = int(input('b = '))
c = a / 1.1
day = 0
while c <= b:
    c *= 1.1
    day += 1
    print(day, '-iy den: ', round(c, 2))
print('otvet: na ', day, '-iy den sportsmen dostig resultata - ne menee ', b, ' km')
