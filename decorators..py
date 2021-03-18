

#HARRY KE CODES.

# def function1():
#     print("Subscribe now")
#
# func2 = function1
# del function1
# func2()

# def funcret(num):
#     if num==0:
#         return print
#     if num==1:
#         return sum
#
# a = funcret(1)
# print(a)

# def executor(func):
#     func("this")
#
#
# executor(print)

#def dec1(func1):
#    def nowexec():
#        func1()
#        print("Executed")
#    return nowexec

#@dec1
#def who_is_harry():
#    print("Harry is a good boy")

# who_is_harry = dec1(who_is_harry)

#who_is_harry()

#def inner1(func):
#    def inner2():
#         print("Before function execution")
#         func()
#         print("After function execution")return inner2

#@inner1
#def function_to_be_used():
#    print("This is inside the function")

#function_to_be_used()



# MY FUNCTIONS AND PRACTICES.




print("ANIKET KE COOES ON DECORATOR.")
def ja(func):
    def ka():
        print("KALL IS A KUTTA.")
        #ja(func)
        func()
        print("NIKKAL")
    return ka
    #return ka
#ja()
#SIMPLE LIFE:
def kall():
    print("CHALO TOH SURU KARTE HAI.")
    return kall
kall()
kall=ja(kall)
#kall=ja(kall())
kall()
#NOW IT IS TIME FO MENTOS LIFE.
@ja
def kall():
    print("CHALO TOH SURU KARTE HAI.")
    return kall

#kall=ja(kall)
#kall=ja(kall())
kall()




