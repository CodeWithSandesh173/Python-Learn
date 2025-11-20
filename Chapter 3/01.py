#list
l1=[
    "Sandesh",
    9860801769,
    21.21,
    "Bhandari"
]
print(type(l1)) #it will give you list
#how to print 9860801769 from list
#we have to know about index number starts from 0 here is example
"""
Items            Index Number
Sandesh    =     0
9860801769 =     1
21.21      =     2
Bhandari   =     3
"""

print (l1[1]) #you can do for all
print (l1) #GIVES ['Sandesh', 9860801769, 21.21, 'Bhandari']
print ("\n") #to left one line
for i in l1: #this is loop and will taught in chapter 5
    print (i) #prints all element