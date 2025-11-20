number = int(input("Enter a number: "))
s = number
product = 1

while number != 0:
    digit = number % 10        # get last digit
    product *= digit           # multiply it to product
    number //= 10              # remove last digit

print(f"Product of digits of {s} is {product}")
