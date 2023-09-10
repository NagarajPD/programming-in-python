#return_value
def add_2_nos(x,y):
    return(x+y)



x=1
y=6

z=add_2_nos(x,y)
print(z)

def add_2_no_sqr(x,y):
    t=add_2_nos(x,y)
    print(t*t)

add_2_no_sqr(3,2)