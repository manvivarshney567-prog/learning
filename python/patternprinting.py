# ques 1.
 
n=5
for i in range(n):
   for j in range(n):
      print("*", end=" ")
   print( )
 
# ques 2.
 
n=5
for i in range(1,n+1):
   for j in range(i):
      print("*",end=" ")
   print()  



# ques 3.

n=5
for i in range(n,0,-1):
   for j in range(i):
      print("*",end=" ")
   print()


#ques 4.
n=5
spaces=n-1
star=1
for i in range(1,n+1):
    for j in range(1,spaces+1):
        print(" ",end=" ")
    for j in range(1,star+1):
        print("*",end=" ")
    print()
    star+=1
    spaces-=1


#ques 5.
n=5
spaces =0
star =n
for i in range(1,n+1):
    for j in range(1,spaces+1): 
        print(" ",end=" ")
    for j in range(1,star+1):
        print("*",end=" ")
    print()
    star-=1
    spaces+=1

# ques 7.

n=5
for i in range(n):
   for j in range(n):
      if i==0 or i==n-1 or j==0 or j==n-1:
         print("*",end="")
      else:
         print("",end="")
      print()   


# ques 8.
for i in range(1,n+1):
   for j in range(1,n+1):
      if 1 ==j or i== (n-j+1):
         print("*",end=" ")
         
