d={
    "Sandesh":"Bhandari",
    "Samip":"Adhikari",
    "Saugat":"Subedi",
    "Sita":"Mata"
}
d["Samrat"]="Poudel" #add new key and value
print (d)                                  
del d["Sita"]     #to remove key Sita along with value      
print (d)  

#lets print value
print (f"Samip ko cast ho {d['Samip']}")

#to add more key and value
d.update({
    "Krishna":"Radha",
    "Ram":"Sita"
})

print (d)

# to print all without {}
for i in d:
    print (i) #it print key
for j in d:
    #to print values only
    print (d[j])
#to print key with values
for x in d:
    print (x,d[x])