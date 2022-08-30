fruits=[]

fruits.append('Mango')
fruits.append('Apple')
fruits.append('Banana')
fruits.append('Guava')

print(fruits)


fruits.insert(1,'Orange')
print(fruits)

# extend function
dry_fruits=['Almonds', 'Cashew', 'Walnut','Dates','Raisins']
fruits.extend(dry_fruits)
print(fruits)

# Sort function

fruits= ['Cherry','Guava','Apple','Banana']
fruits.sort()
print(fruits)

# remove function
fruits= ['Cherry','Guava','Apple','Banana']
fruits.remove('Apple')
# fruits.remove('Dragonfruit')
print(fruits)

# Reverse Function
fruits= ['Cherry','Guava','Apple','Banana']
fruits.sort(reverse = True)
print(fruits)