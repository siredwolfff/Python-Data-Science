a = [1,2,3,3,1,2,3,1,12,1,2,3,1,3,1,5,5,4,1,1,1,1,2,2]

clean_a = list(filter(lambda i: i != 1, a))
print(clean_a)


files = ['a.png', 'b.png', 'c.png', 'd.png']
jpeg = list(filter(lambda name: name.endswith('.jpg'),files))
png= list(filter(lambda name: name.endswith('.png'),files))
print(jpeg)
print(png)
