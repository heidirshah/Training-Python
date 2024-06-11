x = int(input("Enter a number:\n"))

if x > 10:
    print("x is bigger than 10")

    if x%2 == 0:
        print(x,"is even number")
    else:
        print(x,"is odd number")

else:
    print("x is less than 10")