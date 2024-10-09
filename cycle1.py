import math

a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
h = float(input("Введіть h: "))

for x in range(int(a), int(b), int(h)):
    if x < 0:
        print("f(",x,") не існує")
    else:
        try:
            fx = round(math.log10(abs(x+math.sqrt(x))),2)
            print("f(",x,") = ", fx)
        except:
            print("error")
