x=[1,2,3,4,5,6,7,8,9123]

def foo(t,*args,**kwargs):
    print(t)
    print(args)
    print(kwargs)

foo(x,899,0,9,8,5,7,5,4,3,23,monday=99,tuestady=23456,wednesday=87654)