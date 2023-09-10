candidates=['anil','kiran','manish','rina']
print(candidates)
print(candidates.index('manish'))
candidates.insert(candidates.index('rina'),'mohan')

print(candidates)
candidates.pop(candidates.index('kiran'))
print(candidates)
candidates.remove('anil')
print(candidates)




items={"items":"hard disk","price":"2000","model":"aabbcc"}
print(items)

for i in items.keys():
    print("the {} is {}".format(i,items.get(i)))
