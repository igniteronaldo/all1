







text = "Python tutorial for absolute beginners."
t = text.split()
print(t)

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_dash(cls,string):
          return cls(*string.split("-"))

date1=Date.from_dash("2008-12-5")
print(date1.year)


class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        # params = string.split("-")
        # print(params)
        # return cls(params[0], params[1], params[2])
        return cls(*string.split("-"))


harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 455, "Student")
karan = Employee.from_dash("Karan-480-Student")

print(karan.no_of_leaves)
# rohan.change_leaves(34)
#
# print(harry.no_of_leaves)



#PRACTICE


ra="pro ki toh hi hai bjhaiyaji yeh gamer"
#print(ra.split())


class Faltu:
    def __init__(self,friend1,friend2,friend3,friend4,friend5):
        self.bheem=friend1
        self.chutki=friend2
        self.bholu=friend3
        self.dholu=friend4
        self.kalia=friend5
    @classmethod
    def for_all_friends(cls,friends):
        return cls(*friends.split("-"))
def dholak(dholaka):
    def kallu_bhai():
        print(format("AAPKA SWAGAT HAI HAMARE AAPKE SABKE PYARE"))
        dholaka()
        print("AAIYE AUR CHAAA JAIYE YAHA PAR ,HAN JI BILKUL.")
    return kallu_bhai
@dholak
def info():
    print("dholakpur dham dhama dham dham dholakpur")
    return info
info()
print("WHAT IS YOUR NAME.")
name=input(("Please Enter Your Name here:"))
age=int(input(("Please Enter Your age here:")))
print(f"AA JAO MERE MAHARAJ{name} AAPKA HUME BADE JORO SORE SE INTEZAR THA, KYUNKI HUME AAPKA UMRA PATA HAI JO KI HAI{age}")
frienks=Faltu.for_all_friends("bheem-chutki-bholu-dholu-kalia")
heroes="ye humare dholakpur ke kuch chote packet bade dhamake karne wale visphotak dynamiyte wale bache hai."
information1="aaiye mai aaplko inse milwata hu:"
print(heroes.capitalize())
print(information1.capitalize())
person1="ye hai sabse sur veer yodha:"
print(person1.capitalize(),frienks.bheem)
person2="ye hai sabse lambi choti wali ladki:"
print(person2.capitalize(),frienks.chutki)
person3="ye hai anokha bache jaise dikhne wala part2:"
print(person3.capitalize(),frienks.dholu)
person4="ye hai anokha bache jaise dikhne wala part1:"
print(person4.capitalize(),frienks.bholu)
more_info="yeh dono hi bhai hai,mera matlab dholu aur bholu."
print(more_info.capitalize(),"aur yahi toh sachai bhi hai mere pyare aur nirale maharaj in dono ke beech ka maharaj",name,"\nAage chalte hai yaha ke shoorveer aakhri ke paas mai.")
person5="ye kabhi na har marne wala aur bheem jaise bacho ko ura ura ke marne wala:"
print(person5.capitalize(),frienks.kalia)