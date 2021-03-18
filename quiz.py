#for while loop quiz no 1
#print("enter  your name please")
#ing=input("here:")
#try:
#  print("enter your age please")
#  inp=int(input("here:"))ULD ENTER YOUR AGE BUT ITS YOUR CHOICE NOW JU
# #except:
#    #  print("BUT I THINK U SHOST CONTINUE FURTHER",ing.capitalize())


#print("Hello",
 #     ing.capitalize())

#print("thanks for giving us some of your details.\n")
#print("you only have one opportunity to eneter a number over 100 \n"
#      "better use it wisely.SORRY I WAS JOKING MY FRIEND",ing.capitalize())

#while (True):
#       usernumber = int(input("please enter only one number which is greater than 100\n"
 #                             "here:"))
 #      if  usernumber>100:
 #           print("congratulations , entered a number greater than hundred")
 #           break
 #      else:
 #           print("please enter your number again,\n"
 #                 "your number was smaller then 100\n")
 #           continue
#print("THANKS FOR USING THIS FUN SOFTWARE MY FIRNED\n"
 #     "U ARE JUST TRULY GREAT\n"
 #     "U ARE NOW A PART OF\n "
 #     "TIWARI AND CO.\n"
 #     "THANKS AGAIN\n")



print("quiz 2")

# 0 1 1 2 3 5 8 13


def kallu(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return kallu(n-1) + kallu(n-2)

w= int(input("so type your number:"))
print(kallu(w))
















# 0 1 1 2 3 5 8 13
def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci (n - 1) + fibonacci (n - 2)


number = int (input ("Enter then number"))
# print("Factorial Using Iterative Method", factorial_iterative(number))
# print("Factorial Using Recursive Method", factorial_recursive(number))
print (fibonacci (number))
















