while True:
    n = int(input("n= "))
    m = int(input("m= "))
    k = int(input("k= "))
    s = (n * m)
    if k < s:
        if k % n == 0 and k >= n:
            print("YES")
        elif k % m == 0 and k >= m:
            print("YES")
        else:
            print("NO")
    else:
        print("stop")
