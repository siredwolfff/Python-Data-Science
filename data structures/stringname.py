name = 'Vijay Deenanath Chauhan'
#first name
firstname = name[:7]
print(firstname)
lastname = name[-5:]
print(lastname)
middlename = name[7:-6]
print(middlename)
even_index = name[::2]
print(even_index)
odd_index = name[1::2]
print(odd_index)

reversed_name = name[::-1]
print(reversed_name)

print(name[:]) #wont affect
print(name[::-1][:7][::-1])


