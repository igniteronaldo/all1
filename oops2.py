def read_number(self):
    print (self.num)
# body of the constructor

class Person:
    def __init__(self, name, age):
      self.name = name
      self.age = age


p1 = Person ("John", 36)
print (p1.name)
# Output: John

#main
class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"


harry = Employee("Harry", 255, "Instructor")

# rohan = Employee()
# harry.name = "Harry"
# harry.salary = 455
# harry.role = "Instructor"
#
# rohan.name = "Rohan"
# rohan.salary = 4554
# rohan.role = "Student"

print(harry.salary)
print(harry.printdetails())


#practice

class fel:
    def __init__(self,obsession,life,purpose,passion):
        self.obsession=obsession
        self.life=life
        self.purpose=purpose
        self.passion = passion

    def papad(self):
        print("janlo apne bare mai")
        return self.passion,self.obsession,self.purpose,self.life,"are real good friends of life"

    def jeng(self):
        print(self.life,"are good friends when they play together.")
        return "rahul ki toh !!!!!!!!"

ga = fel ("atom", "banton", "galon", "rapon")
print(ga.passion)
print(ga.papad())
print(ga.jeng())
try:
    print(parmanandu,"is",andu )
except Exception as luck:
     print(luck)

def j(string):
    print("rahu",string)
    return "bas re bas"
print(j("sjsjs"))



