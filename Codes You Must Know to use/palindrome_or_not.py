# take input from the user
num = int(input("Enter a number: "))
original_num = num
reversed_num = 0

while num > 0:
    digit = num % 10            # get last digit
    reversed_num = reversed_num * 10 + digit
    num = num // 10             # remove last digit

# check if original number and reversed number are same
if original_num == reversed_num:
    print(f"{original_num} is a palindrome")
else:
    print(f"{original_num} is not a palindrome")
