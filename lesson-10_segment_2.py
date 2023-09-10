


x=90
y=0


try:
    print(x/y)
except ZeroDivisionError:
    print("division by 0 error")
finally:
    print("this is a finally block")


print("rest of the code")

#in a kitchen if the temp of the oven goes beyond 400 def F ,
#then the exectption should be raised

class FireAlret(Exception):
    def show_alret(self):
        print("the temp has gone beyond 400 !!!")

        

def cook(temp):
    if temp>400:
        raise FireAlret

    else:
        print("cooking in progress")


try:
    cook(412)
except FireAlret:
    print("fire fire alret")
finally:
    print("this is finally block")


