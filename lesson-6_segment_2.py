#INHERITANCE

class Emp:
    emp_name=""
    emp_code=""
    salary=0
    def accept_data(self):
        self.emp_name=input("enter emp name")
        self.emp_code=input("enter emp_code")
        self.salary=int(input("enter salary"))
    def show_data(self):
        print("emp name ",self.emp_name)
        print("emp_code ",self.emp_code)
        print("emp name ",self.salary)

class perm_emp(Emp): #in inhertance base calss is mentiomned inside abarcket 
    mgrid=""
    dept_id=""
    def accept_data(self):
        Emp.accept_data(self)
        self.mgrid=input("enter mgr id ")
        self.dept_id=input("enter deptid ")

    def show_data(self):
        Emp.show_data(self)
        print("mgrid",self.mgrid)
        print("dept id",self.dept_id)


class cont_emp(Emp):
    supervisor_id=""
    agency_id=""
    def accept_data(self):
        Emp.accept_data(self)
        self.supervisor_id=input("enter the supervisor ID")
        self.agency_id=input("enter the agency ID")

    def show_data(self):
        Emp.show_data(self)
        print("supervisor ID ",self.supervisor_id)
        print("agency ID ",self.agency_id)

        



#Create object of the permanent employee
employee1=perm_emp()
employee1.accept_data()
employee1.show_data()


#Create object of the contract employee
employee2=cont_emp()
employee2.accept_data()
employee2.show_data()