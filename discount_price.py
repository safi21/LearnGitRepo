origPrice = float(input("Enter the price $"))
discount = float(input("Enter the discount $"))
mPrice = (1 - discount / 100) * origPrice
print(
    "The price of {:.2f} after {:.2f} discount is ${:.2f}".format(
        origPrice, discount, mPrice
    )
)
