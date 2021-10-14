import math
a = int(input('Вводи сторону,чел:'))
b = int(input('Вводи сторону,чел:'))
c = int(input('Вводи сторону,чел:'))
def sow_all():
    p = (a + b + c)/2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print('Площадь равна', s)
sow_all()
