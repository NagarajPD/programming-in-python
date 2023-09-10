itemas=["BAN1234","MUM98765432","CHE12096543","HYD72599"]
for t in itemas:
    print(t[0:4])




x=[8,1,2,9,3,5,6,7,8]
y=sorted(x)
print("y=",y)
print("x=",x)
x.sort() #METHOD
print("x=",x)


x=[10,20,30,40,50]
print("x=",x)
y=reversed(x)
print("y=",(list(y)))
x.reverse()
print("x=",x)


x=[10,20,30,40,50]
print(max(x))
print(min(x))