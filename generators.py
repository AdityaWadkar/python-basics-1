# example one

def gencubes(n):
    for num in range(n):
        yield num**3

for x in  gencubes(10):
    print(x)

    # Generators are best for large set of data

# fibo

def fibo(n):
    
    a = 1
    b = 1
    for x in range(n):
        yield a 
        temp = a
        a = b
        b = b + temp

for num in fibo(10):
    print(num)



# using it without generators

print('next')

def fibo1(n):
    
    a = 1
    b = 1
    for x in range(n):
        
        temp = a
        a = b
        b = b + temp
        print(a)
        
    

print(fibo1(10),"dusre se")



# using with generators but with tuples
print("Tuple")

def febo_tup(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b,a+b

for num in febo_tup(10):
    print(num)
