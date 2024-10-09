import math

a = float(input("a: "))
b = float(input("b: "))
h = float(input("h: "))

x = a

while x <= b:
    fx = math.log10(abs(x + math.sqrt(x)))
    fx=round(fx,2)
    print(x," ",fx)
    x += h
    if x >=b:
        break