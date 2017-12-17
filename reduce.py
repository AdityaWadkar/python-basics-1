from functools import reduce

# so now we will be doing Reduce , which will reduce it to singular answer.
list1 = [1,2,3,4,5,6,7,8,5445,65,634,5345,34]

red = reduce(lambda x,y : x+y ,list1)
print(red)


# as simple as it is :D


