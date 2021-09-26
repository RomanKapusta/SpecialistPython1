a = int(input("a= "))
i = 0
if 2 < a <= 30:
    print("#" * a)
    while i < a - 2:
        print("#", " " * (a-4), "#")
        i += 1
    print("#" * a)
else:
    print("Warning")
