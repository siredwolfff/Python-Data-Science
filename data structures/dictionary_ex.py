my_dict= {'name': 'Jack', 'age': 26}
# print(my_dict)

# print(my_dict.get('age'))

# print(my_dict['address'])

# print(my_dict.get('address'))

# update value

my_dict['age']= 27
print(my_dict)
my_dict['address']= 'Downtown'
print(my_dict)

# removing elements from dictionary

squares= {1:1,2:4,3:9,4:16,5:25,6:36}
# print(squares.pop(4))
# print(squares.popitem())
# squares.clear()
# del squares

# iterating through a dictionary
squares= {1:1,2:4,3:9,4:16,5:25}
for i in squares:
    print(i)

for i in squares:
    print(squares[i])

for k,v in squares.items():
    print(k,v)

# create a dictionary for storing student report which contain marks of different subjects

st_dict= {'A': s1': 50, 's2': 60, 's3':70, 's4':80, 's5':90,{'B': s1': 50, 's2': 60, 's3':70, 's4':80, 's5':90}}
print(st_dict)




