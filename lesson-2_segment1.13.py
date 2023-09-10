c1=input("You are an ___________ citizen")
c2=input("wt is your age ")


c2=int(c2)
if c1=="indian" and c2>=18 :
    print("selected")
elif c1=="NRI" and c2>=18:
    print("selected")
else:
    print("not selected")