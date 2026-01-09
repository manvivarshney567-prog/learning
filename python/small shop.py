
queue = []
token = 1 

while True:

    print("\n1.Add customer")
    print("\n2.Serve customer")
    print("\n3.show Queue")
    print("\n4.Exit")

    choice = int(input("enter your choice:"))

    if choice==1:
        queue.append(token)
        print("customer added:",token)
        token +=1

    elif choice==2:
        if queue:
            print("Serving customer:",queue.pop(0))
        else:
            print("no customer:")

    elif choice==3:
        if queue:
            print("current queue:",*queue)

        else:
            print("Queue is empty.")

    elif choice==4:
        print("thank you!")
        break
    else: 
        print("choice invalid")
