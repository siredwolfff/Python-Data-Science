from functools import reduce
import operator

x = [2,1,3,4,5,4,1,2,1,3]

# multiply all value of x

ans = reduce(operator.mul, x)
print(ans)

# # same as
# ans = 1
# for i in x:
#     ans *= i
# print(ans)

ans2 = reduce(lambda i,j: i+i*j+i, x)
print(ans2)


