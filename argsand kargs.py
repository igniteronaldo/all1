
#     print(a, b, c, d, e)

def funargs(normal, *argsrohan, **kwargsbala):
    print (normal)
    for item in argsrohan:
        print(item)
    print ("\nNow I would Like to introduce some of our heroes")
    for key, value in kwargsbala.items ():
        print (f"{key} is a {value}")


# function_name_print("Harry", "Rohan", "Skillf", "Hammad", "Shivam")

har = ["Harry", "Rohan", "Skillf", "Hammad",
       "Shivam", "The programmer"]
normal = "I am a normal Argument and the students are:"
kw = {"Rohan": "Monitor", "Harry": "Fitness Instructor",
      "The Programmer": "Coordinator", "Shivam": "Cook"}
funargs(normal, *har, **kw)
def chung(asha,*pasha,**tasha):
    print(f"{asha}is different from{pasha} and this is also different from{tasha}")

gasa=1,2,3
masa=4,5,6
nasa={"fas":"fish","first":"gish","thus":"tish"}
chung(gasa,*masa,**nasa)







