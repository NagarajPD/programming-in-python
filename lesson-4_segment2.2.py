rainfall={"kar":12,"mah":20,"ker":22,"tn":23}
max_rain=max(rainfall.values())
min_rain=min(rainfall.values())
for s in rainfall.keys():
    if rainfall.get(s)==max_rain:
        print("max rain in ",s)
    elif rainfall.get(s)==min_rain:
        print("min rain in ",s)



r=[2,1,5,7,2,3] #iterator

def sq(x):
    return x*x

y= map(sq, r)
print(list(y))



r=[2,1,5,7,2,3] #iterator

y= map(lambda u: u*u, r)
print(list(y))



a=[1,2,3,4,5]
b=[6,7,8,9,0]

#multiply each item from "a" wirh corresponding itam with "b"
#output shd be [6,14,24,36,0]

c=map(lambda u,v:u*v,a,b)
print(list(c))

#filter function
a=[2,3,5,6,12,1,6,13,22,44,88]
b=filter(lambda x:x>10,a)
print(list(b))


#assignmemnt
#in the above list wt is the sum of all numbers more than 10
a=[2,3,5,6,12,1,6,13,22,44,88]
b=filter(lambda x:x>10,a)
print(list(b))
c=list(b)
for i in c:
    z=1+c
    print(c)