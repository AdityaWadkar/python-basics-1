# so lets talk about map in python, it is very easy to use , just mention the function and the mapping to it
list1 = [1,2,3,4,5,6]

square = list(map(lambda x : x**2,list1))
print(square)

# alert , if you dont put list , it will return object to save space