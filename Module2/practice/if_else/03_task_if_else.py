while True:
    a = int(input("a= "))
    b = int(input("b= "))
    c = int(input("c= "))
    if a * b == b * c:
        print("YES")
    elif b * c == c * a:
        print("YES")
    elif c * a == b * a:
        print("YES")
    else:
        print("NO")
