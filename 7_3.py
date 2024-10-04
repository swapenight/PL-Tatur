import math

def gip(a, b):
    return math.sqrt(a**2 + b**2)

c1 = float(input('Введите длину первого катета: '))
b1 = float(input('Введите длину второго катета: ', '\n'))
gip1 = gip(c1, b1)

c2 = float(input('Введите длину первого катета: '))
b2 = float(input('Введите длину второго катета: ', '\n'))
gip2 = gip(c2, b2)

if gip1 > gip2:
    print('Гипотенуза первого треугольника больше')
elif gip2 > gip1:
    print('Гипотенуза второго треугольника больше')
else:
    print('Гипотенузы равны')

#------------------------------------------------------------------------------------------------------------------------

def sw(t):
    w = t.split()
    for i in range(len(w)):
        w[i] = ''.join(sorted(list(w[i])))
    return ' '.join(w)

t = input('Введите строку: ')
r = sw(t)
print('Отсортированная строка: ', r)