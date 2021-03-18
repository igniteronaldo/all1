


# Lambda functions or anonymous functions
#def add(a, b):
#    return a+b
#print(add(int(input("type num1")),int(input("type num2"))))

#minus = lambda x, y: x-y

#def minus(x, y):
#    return x-y
#    #return x+y
#print(minus(int(input("type num1")),int(input("type num2"))))


a = [[1, 14], [5, 6], [8, 23]]
a.sort (key=lambda x: x[1])
print (a)


def aaa():
#list.sort(key=lambda,reverse=True|False)
     result = lambda n1, n2, n3: n1 + n2 + n3
     print ("Sum of three values : ", result( 10, 20, 25 ))
     return result
print(aaa())


rahul=lambda pa,ka:pa+ka
print(rahul(int(input("type number 1")),int(input("type number 2"))))

