number = int(input("Enter a number: "))
s = number
j = 0

while number != 0:
    r = number % 10
    j = j + r**3
    number //= 10

if s == j:
    print("The number is an Armstrong number")
else:
    print("The number is not an Armstrong number")
