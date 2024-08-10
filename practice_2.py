class employ:
    def __init__(self, role, salary, dept):
        self.role = role
        self.salary = salary
        self.dept = dept

    def showDetails(self):
        print("Role : ", self.role)
        print("Salary :", self.salary)
        print("Department:", self.dept)

class engineer(employ):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Engineer","Production","75822")
# e1= employ("Engineer","40000","Food processing")
# e1.showDetails()
eng=engineer("Sajid ","24")
eng.showDetails()
