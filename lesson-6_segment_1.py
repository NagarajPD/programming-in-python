#ENCAPLSULATION

class account:
    acc_number="123467890"
    deposit=9876432
    loans=23456789
    password="abc123"

sunil=account()
print(sunil.deposit)
 

#DETAILS ARE DONE PRIVATE HERE
class account:
    acc_number="123467890"
    __deposit=9876432
    __loans=23456789
    __password="abc123"

sunil=account()
print(sunil.deposit)




#DETAILS ARE DONE PRIVATE HERE ONLY OWNER CAN SEE IT
class account:
    acc_number="123467890"
    __deposit=9876432
    __loans=23456789
    __password="abc123"

    def show_deposits(self):
        p=input("enter password")
        if p=="apple":
            print(self.__deposit)
        else:
            print("acces denaied")
 
sunil=account()
sunil.show_deposits()

 