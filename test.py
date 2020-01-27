while True:
    try:
        while True:
            startPoint = int(input("Enter starting point : "))

            if startPoint > 0:
                continue
            else:
                print("The number of cars cannot be less than zero")
        break
    except:
        print("This is a string")
    try:
        while True:
            startPoint = int(input("Enter starting point : "))

            if startPoint > 0:
                continue
            else:
                print("The number of cars cannot be less than zero")
        break
    except:
        print("This is a string")