x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))
if x > y:
    if x > z:
        print(x, "is max")
    else:
        print(z, "is max")
else:
    if y > z:
        print(y, "is max")
    else:
        print(z, "is max")