a=1
b=5
for row in range(1,6):
    for col in range(1,10):
        if(col>=a and col<=b):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    a=a+2
    b=b+1
    print( )
