
class Employee:
    def __init__(self,name,role,salary):
        self.name=name
        self.role=role
        self.salary=salary
    def printemp(self):
        return self.salary,self.name,self.salary,self.role,"is a good boy."


class copy(Employee):
    def __init__(self,name,role,salary,pet,house_income):
        self.name=name
        self.role=role
        self.salary=salary
        self.pet=pet
        self.house_income=house_income

    def printcop(self):\
        return "BHARAT",self.name,"ka desh hai"

kar=Employee("rahua","hahah",7777)
har = copy('rahu', str ("programmer"), 10000,"dog",100000000)

print (har.printemp ())
print(har.printcop())
print(har.name)