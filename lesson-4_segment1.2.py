u=[23,34,42,23,32]
t=0
def show_biggest(x):
    global t
    for i in x:
        if i>t:
            t=i
    print(t)


show_biggest(u)

g=[99,66,100,12]
show_biggest(g)


x=90
def test_fn():
    x=30
    print(x)

test_fn()


x=90
def test_fn():
    global x
    print(x)
    



def test_abc():
    global x
    print(x)
test_fn()
test_abc()



x=90
def test_fn():
    global x
    print(x)
    x=900
    



def test_abc():
    global x
    print(x)

def test_z():
    print(x)

test_fn()
test_abc()
test_z()