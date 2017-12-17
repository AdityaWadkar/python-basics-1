# list exampls 

my_list = ['ashish',123,1.232,'popu',123,567,'jugo','sandwitch']
print(my_list)

# length of list

print(len(my_list))

# indexing of list

print(my_list[1])
print(my_list[1:])
print(my_list[:3])
print(my_list[1::2])
print(my_list[::-1])


# poping items
# pop_list = my_list.pop(2)
# print(pop_list)
print(my_list)


# reverse string


reverse_string = my_list[::-1]
print(reverse_string)


# in python lists support nesting i.e it supports lisi inside list
list1 = ['ace','ash','rishu']
list2 = ['nami','baby','babda']
list3 = ['popu','gopu','bubloo']

main_list = [list1,list2,list3]
print(main_list)
print(main_list[2][1])

# dictionaries in python ,and we can consider it as hash table

dict1 = {'key1':'ace','key2':[19,2223,'ashish'],'key3':[[123,234],[343],1]}
print(dict1.keys())
print(dict1.values())
print(dict1['key2'][0])
print(dict1['key3'][0][1])
dict2 = {'ace':'bc'}
print(dict2.values())
dict2['ace'] = 'ashish'
print(dict2.values())

print(dict2.keys())

#tuples in python : they are immutable i.e cant be changed

# its same as lists and we only need to use it we want to immutate somrthing chillaxxxx



# set in python
# sets are used if want no repetition
list_repeat = [1,2,3,4,53,523,2,312,31,412,3,11,2,1,1,1,1,1,1,1,2,2,2,3,3,4,4,55,6]
print(set(list_repeat))
