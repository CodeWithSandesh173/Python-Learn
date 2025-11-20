#list
l1=[
    "Sandesh",
    9860801769,
    21.21,
    "Bhandari"
]
#to add new element
l1.append("Nepal") #it add to last index number
print (l1)

l1.extend(["Pokhara", "Dhikurpokhari"]) #it will add multiple elements
print (l1)

l1[0]="God" #to give new element to 0 index number
print (l1)
l1.pop(3) #to remove element by index number
print (l1)

#to reverse list
(l1.reverse())
print (l1)
#to find length
print (len(l1))