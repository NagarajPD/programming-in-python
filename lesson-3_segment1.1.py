for i in range(5):
    x=int(input("eneter any positive number  "))
    if x>=0:
        print(x*x*x)
    else:
        print("you have enteered a -ve number,please try again")
        continue
    print("this is rest of the code")
    print("this is also a test message123")


for i in range(10):
    for j in range(10):
        if j==5:
            break
        print("j=",j,end=" ")
    print("i=",i)
         








