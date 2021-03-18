
# n! = n * n-1 * n-2 * n-3.......1
# n! = n * (n-1)!
def factorialchalo(n):
    """
        :param n: Integer
        :return: n * n-1 * n-2 * n-3.......1 1*2*3
    """

    fac = 1
    for i in range(n):
        fac = fac * (i + 1)
    return fac


n=int(input("write your number."))
print(factorialchalo(n))



def factorial_recursive(n):

      if n == 1:
         return 1
      else:
          return n * factorial_recursive (n - 1)
why=int(input("type your number"))

print(factorial_recursive(why))

#factorial_recursive(5)
    # 5 * factorial_recursive(4)
    # 5 * 4 * factorial_recursive(3)
    # 5 * 4 * 3 * factorial_recursive(2)
    # 5 * 4 * 3 * 2 * factorial_recursive(1)
    # 5 * 4 * 3 * 2 * 1 = 120


# 0 1 1 2 3 5 8 13
#def fibonacci(n):
#    if n == 1:
#        return 0
 #   elif n == 2:
  #      return 1
  #  else:
  #      return fibonacci (n - 1) + fibonacci (n - 2)


#number = int (input ("Enter then number"))
# print("Factorial Using Iterative Method", factorial_iterative(number))
# print("Factorial Using Recursive Method", factorial_recursive(number))
#print (fibonacci (number))

tac = 1
for i in range(3):
    tac=tac*(i+1)
    print (i)
print(tac)
#1*2*3

