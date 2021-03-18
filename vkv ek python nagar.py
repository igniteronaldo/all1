#PEHLA QUIZ 1:
#USING BOTH FOR FOR AND WHILE LOOP PRINT FIRST 100 NATURAL NUMBERS.
#CREATE A LIST TO STORE NAME OF YOUR FRIENDS AND DISPLAY THEM USING LOOP.
#USING RANGE() PRINT EVEN NUMBERS TILL 50.

#FOR FIRST


natural_numbers=1
while (natural_numbers<=100):
      print(natural_numbers)
      natural_numbers=natural_numbers+2
      continue

#FOR SECOND

name1=input("PLEASE ENTER YOUR NAME:")
name2=input("PLEASE ENTER YOUR NAME HERE:")
l={1:name1,2:name2}
for g,v in l.items():
    print("PRESS",g,"for",v,".")
name=int(input("PRESS THE NUMBER FOR DISPLAYING YOUR NAME:"))
print("WELCOME",l[name].capitalize(),".I AM FINE.\nHOW ARE YOU?")
i=input("\nPRINT ENTER HOW ARE U HERE:")
print("I AM ALSO JUST LIKE,",i.capitalize(),".")
print("THANKS",l[name].capitalize(),".")


# FOR THIRD.
fac=0
for qw in range(26):
    print ("TOH YEH RAHA AAPKA NUMBER AAP KE COMPUTER SCREEN PAR:", fac, "")
    fac=fac+2
    continue
print(f"YEH LOJI AAGAYA APKA DOST GOOGLU NUMBER LEKAR",l[name],".")






