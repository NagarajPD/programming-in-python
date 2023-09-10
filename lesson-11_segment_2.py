def greet(guest):
    print(guest)

def mygreet(fn):
    def temp(fn):
        print("welcome mr ",fn,"to abc company")
    return temp

greet =mygreet(greet)

greet('nagaraj')