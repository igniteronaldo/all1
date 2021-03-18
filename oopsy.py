#pass is equal to kuch nahi.
class MyClass:
    '''This is a docstring.'''
    pass
class india:
    great=input("1.How great are you tell me:i mean india :")
    why=input("1. what is the best thing about india.")
    pass
print(india)
forum1=india
forum1.great=india.great
forum1.why=india.why
print(forum1.__dict__)
print(forum1.great)
print(forum1.__dict__)
print(forum1.__dict__)
print(forum1.why)
print(forum1.__dict__)
print("WELCOME:",forum1.great,"of age ",forum1.why)
class Student:
    pass

harry = Student()
larry = Student()

harry.name = "Harry"
harry.std = 12
harry.section = 1
larry.std = 9
larry.subjects = ["hindi", "physics"]
print(harry.section, larry.subjects)



