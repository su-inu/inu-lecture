a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
d = int(input('e = '))

print('정렬 전 : ', a, b, c, d)

if a > b : a, b = b, a
if b > c : b, c = c, b
if c > d : c, d = d, c
if a > b : a, b = b, a
if b > c : c, b = b, c
if a > b : a, b = b, a

print('정렬 후 : ', a, b, c, d)
    
