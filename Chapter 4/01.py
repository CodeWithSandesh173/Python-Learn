#conditions to learn operators relation check image at same folder
"""
for single conditions (if else)
for multiple conditions (if elif else)"""

#for sibgle conditiom 
a=int(input("Enter code password: "))
if a==8848:
    print ("Access gained")
else:
    print ("Access denied")

#multiple condtion
#code to find greater number among 2
a=float(input("Enter a number: "))
b=float(input("Enter second number: "))
if a>b:
    print (a,"is greater")
elif (b>a):
    print (b,"is greater")
else:
    print (b,"==",a)