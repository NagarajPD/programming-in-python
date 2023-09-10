x=[]
flag=0
print("enter 10 numbers")
for i in range(10):
        x.append(int(input()))

sr=int(input("which do you want to search"))

for n in x:
    if n==sr:
        flag=1
        break

if flag==1:
    print("number found")
else:
    print("number not found")
    
    