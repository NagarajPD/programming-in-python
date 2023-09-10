items=["mouse","laptop","phone"]
print(items)

marks=[12,23,34]
print(marks)





x=[]
x.append(7)
x.append("india")
x.append(23.456)
print(x)




marks=[]
print("enter marks for 6 subjects")
for i in range(6):
    marks.append(int(input()))
print(marks)




items_ordered=[]
print("enter the items ordered")
for i in range(5):
    items_ordered.append(input())

lap_qty=items_ordered.count("laptop")
print("laptop was ordered for", lap_qty,"times")
