# In this code we will find out the sum of the digits in a number.
x = int(input("Enter a number: "))
sum = 0
while x > 0:
    i = x % 10
    sum = sum + i
    x = int(x / 10)
print(sum)
