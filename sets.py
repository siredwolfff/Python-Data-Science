my_set= {1,2,3}
print(my_set)

# set of mixed datatypes
my_set= {1.0, "Oye", (1,2,3)}
print(my_set)

# creating a set

my_set= {1,2,3,4,3,2}
print(my_set)

my_set= set([1,2,3,4,5])
print(my_set)

# my_set= {1,2,[3,4]}  #will show error
print(my_set)

# initialising a set
a = set()
print()

# initialize my set
my_set= {1,3}
print(my_set)
my_set.add(2)
print(my_set)
my_set.update([1,2,3,4])
print(my_set)
my_set.update([4,5], [1,6,8,9])
print(my_set)

my_set= {1,3,4,5,6}
print(my_set)


my_set.discard(4)
print(my_set)

my_set.remove(6)
print(my_set)

my_set.pop()
print(my_set)

my_set.clear()
print(my_set)