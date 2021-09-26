while True:
    month = int(input("month= "))

    if 3 <= month <= 5:
        print("spring")
    elif 6 <= month <= 8:
        print("summer")
    elif 9 <= month <= 11:
        print("autumn")
    elif month <= 12 and month != 0:
        print("winter")
    else:
        print()
