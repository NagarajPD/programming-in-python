class Cake:
    cake_name=""
    shape=""
    flavour=""
    cost=0

    def accept_data(self):
        self.cake_name=input("Enter name ")
        self.shape=input("Enter shape ")
        self.flavour=input("enter flvour ")
        self.cost=int(input("enter cost "))
    
    def show_data(self):
        print("cake name",self.cake_name)
        print("cake shape",self.shape)
        print("cake flv",self.flavour)
        print("cake cost",self.cost)

#creating objects
c1= Cake() 
c2=Cake()      
c1.accept_data()
c1.show_data()   
c2.accept_data()
c2.show_data()





#ASSIGNMENT
class Laptop:
    item_name=""
    discription=""
    stock=0

    def accepting_data(self):
        self.item_name=input("Enter name ")
        self.discription=input("Enter discription ")
        self.stock=int(input("enter stock "))
    
    def showing_data(self):
        print("item name",self.item_name)
        print("discription",self.discription)
        print("stock present",self.stock)

#creating objects
l1= Laptop() 
l2=Laptop()  
l3=Laptop()      
l1.accepting_data()   
l2.accepting_data()
l3.accepting_data()
print("===========================================")
l1.showing_data()
l2.showing_data()
l3.showing_data()
