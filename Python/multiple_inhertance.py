# 2 ta parents line ani child le 2tai ko inherit garna paryo
class Person:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def show(self):
        print(f"Name : {self.name}\nID : {self.id}")
class Employee():
    def __init__(self,salary):
        self.salary=salary
    def show(self):
        print(f"Salary : {self.salary}")
class Manager(Person,Employee):
    def __init__(self,name,id,salary,experience):
        Person.__init__(self,name,id)
        Employee.__init__(self,salary)
        self.experience=experience
    def show(self):
        Person.show(self)
        Employee.show(self)
        print(f"Experience : {self.experience} yrs")

M = Manager("ram",101,50000,3)
M.show()
