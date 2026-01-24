#   1 2 3 4 5 
# 1 *       *
# 2   *   *
# 3     *
# 4   *   *
# 5 *       *


#   5 4 3 2 1 
# 5 *       *
# 4   *   *
# 3     *
# 2   *   *
# 1 *       *

# row col   row == col   row+col==6
# 1    1      true         false
# 1    5      false        true
# 2    2      true         false
# 2    4      false        true
# 3    3      true         true 

for row in range(1,6):
    for col in range(1,6):
        if(row==col or row+col==6):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print( )


