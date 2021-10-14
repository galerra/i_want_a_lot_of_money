import math
a = 10.2
b = 9.2
x = float(input())
c = 0.5
f = 0
z = 0
def sow_f():
    f = math.log(a + x**2) + math.sin(x/6)
    z = math.exp(-c*x) * (x + math.sqrt(x+a)) / (x - math.sqrt(x-b))
    print(f,z)
sow_f()

