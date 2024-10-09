import math

a = float(input("a: "))
b = float(input("b: "))
h = float(input("h: "))

spisok = []
x = a
while x <= b:
    try:
        fx = round(math.log10(abs(x + math.sqrt(x))),2)
        spisok.append(fx)
    except:
        print("error")
    
    x += h
print("Список значень fx:", spisok)

max_index = spisok.index(max(spisok))
min_index = spisok.index(min(spisok))

print("Індекс найбільшого елемента:", max_index)
print("Індекс найменшого елемента: ", min_index)
    
  