# count function
x = [1,2,3,1,4,1,2,5,5,5,6,1,2,2,7,4,5,6,6,6,6,1,1,2]

print("Total number of 6=", x.count(6))
print("Total number of 2=",x.count(2))
print("Total number of 5=",x.count(5))
print("Total number of 4=",x.count(4))

movies=['Batman','Superman','Avengers','Iron Man', 'DDLJ','Shawshank Redemption', 'GOT', 'KGF', 'Krish']

print(movies.index(('GOT')))
# print(movies.index('Dragon ballZ'))

# copy function
blockbusters= movies.copy()
print("Duplicated list=", blockbusters)

# clear function
# blockbusters.clear()
# print("After clearing Blockbusters=",blockbusters)

# pop function
print("After pop function=", movies.pop())
print("After pop function=", movies.pop(2))
print("After pop function=", movies.pop(4))
print("After popping unavailable index =", movies.pop(12))