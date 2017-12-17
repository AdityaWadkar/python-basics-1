# so ww will be doing list comprehension here
# so below is the long  way how we will impliment it
list1 = []

name = 'ashish'
for i in name:
    list1.append(i)
print(list1)


# now for same thing we will be doing list comprehension


list2 = [i for i in name]
print(list2)


list3 = [i**2 for i in range(1,20)]
print(list3)

# now we will have some if and for both

list4 = [i for i in range(15) if i % 2==0]
print(list4)

list5 = [i**2 for i in [i**2 for i in range(10)]]
print(list5)

# as simple as it is ,
# Holla we are done with it cooolllllllllll!!!!!11