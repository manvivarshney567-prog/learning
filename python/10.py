#    1 2 3 4 5 6 7 8 9 
# 1  * * * * * * * * *
# 2    * * * * * * *
# 3      * * * * *
# 4        * * *
# 5          *



# row    col>=row   col<=2*5-row
# 1          1         9
# 2          2         8
# 3          3         7
# 4          4         6
# 5          5         5

for row in range(1,6):
    for col in range(1,10):
        if(col>=row and col<=2*5-row):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print( )

