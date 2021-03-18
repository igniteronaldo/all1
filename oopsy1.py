
class Employee:
    no_of_leaves = 8
    pass

harry = Employee()
rohan = Employee()

harry.name = "Harry"
harry.salary = 455
harry.role = "Instructor"

rohan.name = "Rohan"
rohan.salary = 4554
rohan.role = "Student"

print(Employee.no_of_leaves)
print(Employee.__dict__)
Employee.no_of_leaves = 9
print(Employee.__dict__)
print(Employee.no_of_leaves)

class Practice:
    pala="rahul is a good boy"
    pass


rahul=Practice.pala
print(rahul)
Practice.pala=Practice.pala,"chal chal chalte hai kahi bahut dur ."
rahul=Employee
print("chalo")
print(rahul.__dict__)
print(Practice)




harry.no_of_leaves=123333333
print(harry.no_of_leaves)
print(Employee.no_of_leaves)


