#    1 2 3 4 5 6 7 8 9 
# 1          *
# 2        * ! *
# 3      * ! * ! * 
# 4    * ! * ! * ! *
# 5  * ! * ! * ! * ! *



# row    5-row+1    5+row-1     (row+col)%2==0 -> print("*")
# 1       5          5                               
# 2       4          6
# 3       3          7
# 4       2          8
# 5       1          9


for row in range(1,6):
    for col in range(1,10):
        if col>=5-row+1 and col<=5+row-1:
            if(row+col)%2==0:
                print("*",end=" ")
            else:
                print("!",end=" ")
        else:
            print(" ",end=" ")
    print()