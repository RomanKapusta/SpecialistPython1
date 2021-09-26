x = float(input("x: "))
i = 0
y = float()
while True:
    i += 1
    y = x * i
    print('%.2f' % float(y))
    if i >= 20:
        break
