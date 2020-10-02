# for loop simple example

l = ['ashish','popu',1,2,3,4,5,6]

for val in l:
    print(val)

    

# one more example 
sequence = range(0,40)
for seq in sequence:
    if seq%2==0 and seq>0:
        print("The number is : ",seq,"and it is even number")
else:
    print("the number is 0")

#Heart Pattern using for loop
for row in range(6):
    for col in range(7):
        if(row==0 and col %3==1)or(row==1 and col%3==0)or(row-col==2)or(row + col==8):
            print("*",end="")
        else:
            print(" ",end="")
    print()

