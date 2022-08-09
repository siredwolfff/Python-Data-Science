#  x= [7,5,3,12]
# x2= []

# for i in x:
#     s= i**2
#     x2.append(s)

# print(x)
# print(x2)

# # for addition of two list

# x= [2,3,5,4]
# y= [3,6,5,3]
# z= []

# for i,j in zip(x,y):
#     z.append(i+j)
# print(z)



# existing list --> new list
# 1. loops
# 2. comprehension(1 line expression)
# 3. lambda expression(later)


#syntax for comprehension

#newlist= [expression    forloop   condition(optional)]


x1= [2,5,8,7,3,6,10]
x2= [i**2 for i in x1]
print(x2)
y= [2,3,5,6,7,8,2]

z= [i+j for i,j in zip(x1,y)]
print(z)

names= ['Bruce Wayne', 'Clark Kent', 'Wally West']
initials= []

for name in names:
    parts= name.split()
    initials.append(parts[0][0]+parts[-1][0])
print(initials)

# using comprehension

names= ['Bruce Wayne', 'Clark Kent', 'Wally West']
initials= [name.split()[0][0]+name.split()[-1][0] for name in names]
print(initials)




