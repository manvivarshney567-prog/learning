#   1 2 3 4 5 
# 1 * * * * *
# 2 *       *
# 3 *       *
# 4 *       *
# 5 * * * * *

# true=*
# false=space

# (row==1) (row==5) (col==1) (col==5)
# row==1 first line 
# row==5 last  line 
# col==1 right side 
# col==5 left side 

for row in range(1,6):
    for col in range(1,6):
        if row==1 or row==5 or col==1 or col==5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()