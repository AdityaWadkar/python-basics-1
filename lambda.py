# SO lets get started with lambda expressions

# firest normal def function
def sum(x,y):
    return (x+y)

print(sum(1,3))

# so we can clearly see its a three liner , so converting it into  a single line 

y = lambda x,y: x+y
print(y(1,2))


# so we have seen how easy it is , just write the logic and then just write the variable names
# only thing to remember is we need to provide label to it , thats it