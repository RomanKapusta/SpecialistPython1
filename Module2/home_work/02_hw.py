while True:
    n = int(input("cow= "))
    if n % 10 == 1:
        print("Корова")
    elif 2 <= n % 10 <= 4:
        print("Коровы")
    else:
        print("Коров")
