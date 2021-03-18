def function1(a,b):
 """yeh lo ji sum aa gaya"""
 a=int(input("type your number"))
 b=int(input("type karo kyun aur ek number nahi hai kya"))
 print(function1.__doc__)
 numbers=sum((a,b))
 print(numbers)
 return numbers
value= function1(4,6)
print(value)
#def function2(a, b):
 #"""toh kaise hai aap log"""
 #average = (a+b)/2
 #print(average)
# return average
#v = function2(5, 7)
#print(v)
#print(function2.__doc__)