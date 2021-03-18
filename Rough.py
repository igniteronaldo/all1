print("enetr tiwari favourite number");
tiwari=input()
print("enter tiwari second favourite number")
aniket=input()
print("i entered",int(tiwari)+int(aniket)+70)
print(type(tiwari))
print(type(int(tiwari)))
print(10*"KAMAKHYA\t")
print(100*"nilesh\n")
nilesh="76"
#print(5*(int("nilesh\n")))
print(10*(int(nilesh)))
truth="asha tiwari"
#print(truth[1:7])
#print(truth[-6:-1])
#print(truth[-6:-1:2])
print(truth[::-2])
print(truth[1:5:-2])
#print(truth[1:7:-1 or -2 or any other thing will not work ])
print(len(truth))
bad="cristiano \n ronaldo"
print(bad)
bad1="cristiano \\ ronaldo"
print(bad1)
bad2="cristiano \'ronaldo"
print(bad2)
bad3="cristiano \r ronaldo"
print(bad3)
bad4="cristiano \b ronaldo"
print(bad4)
bad5="cristiano \f ronaldo"
print(bad5)
bad6="cristiano \" ronaldo"
print(bad6)
bad7="cristiano \a ronaldo"
print(bad7)
bad8="cristiano \v ronaldo"
print(bad8)
good="family"
print(good.isalpha())#returns true only if cahracters are alpahbets whether a to z or A to Z.
print(good.isalnum())
virat="18"
print(virat.isdigit())#it returns true only if characters are digits.
print(virat.isalnum())#it returns true only if characters are digits or alphabets whether a to z or A to Z
chota="tiwari is  good boy"
print(chota.endswith("boy"))
print(chota.capitalize())
print(chota.find("boy"))
print(chota.count("a"))
print(chota.upper())
print(chota.lower())
print(max(chota))
print(chota.find("boy"))
print(chota.replace("boy","son"))



























def dec1(func1):
    def nowexec():
        func1()
        print("Executed")
    return nowexec

