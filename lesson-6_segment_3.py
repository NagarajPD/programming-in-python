#polymorphism

#EXAMPLE__1

class Factory():
    def production(self):
        print("production is 20000")
    def packing(self):
        print("packing without plastic")

class unit1(Factory):
    def production(self):
        print("production is 50000")

class unit2(Factory):
    def production(self):
        print("production is 100000")
    def packing(self):
        print("plastic is used")

ua=unit1()
ub=unit2()

ua.production()
ua.packing()

ub.production()
ub.packing()




#EXAMPLE__2


class A: #base
    def test_fnA(self):
        print("base class")

class B(A): #subclass
    def foo(self):
        print("foo")

class C(A): #subclass
    pass

class D(A): #subclass
    def test_fnA(self):
        print("this is from D class")

#objects

b=B()
c=C()
d=D()

b.foo()
b.test_fnA()

c.test_fnA()

d.test_fnA()