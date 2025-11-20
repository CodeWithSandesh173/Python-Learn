number = int(input("Enter a number: "))
s = number
sum_digits = 0

while number != 0:
    digit = number % 10        # get last digit
    sum_digits += digit        # add it to sum
    number //= 10              # remove last digit

print(f"Sum of digits of {s} is {sum_digits}")
