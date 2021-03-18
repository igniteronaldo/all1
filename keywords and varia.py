# l = 10 # Global
# m=3

# def function1(n):
#    l = 5 #Local
#    m = 8 #Local
#    global l
#    l = l + 45
#    print(l, m)
#   print(n, "I have printed")
# function1("This is me")
# print(m)

# rough work

# a=12 #global



d = 1
def alu():
    global a
    a=1
    a = a + 10
    d = 2
    print("the numbers are", a, "and", d)


alu()
print(a)

x=9
# rough part 2 :
def gillu():
    global x
    x = 7

    def dil():
        global x
        x=4
    print("so the  value of number x in dil is",x)
    dil()
    print("so the  value of number x in dil is",x)
gillu()
print(x)




# x = 89


# def harry():
#  x = 20

#   def rohan():
#      global x
#       x = 88

# print("before calling rohan()", x)
#  rohan ()
#  print ("after calling rohan()", x)


# harry ()
# print (x)
