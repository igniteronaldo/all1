

def ja(names,*lass,**address):
    for jolu in names:
        print(jolu)
    for lolu in lass:
        print(lolu)
    for holu in address:
        print(holu)
print("IF NEW MEMBER THEN TYPOE YOUR NAME.")
c=input("ARE YOU A NEW MEMBER PLEASE TELL US WITH NO OR YES('n' FOR NO AND 'y' FOR YES):")
for juk in c:
    if juk=='y':
        hagamaru=input("PLEASE ENTER YOUR NAME:")
        print("HELLO",hagamaru)
        continue
    else:
         print("HELLO YOU ARE ALREADY A MEMBER OF OUTR SOCIETY,THANK YOU.")
try:
   kavi=["kamakhya","madhu","aniket","nilesh","asha",hagamaru]
   jaba={"kamakhya":"india","madhu":"india","aniket":"india","nilesh":"india","asha":"india",hagamaru:"india"}
   kacha = [1, 2, 3, 4, 5]
   ja (kavi, *kacha, **jaba)

except:
    kavi = ["kamakhya", "madhu", "aniket", "nilesh", "asha", ]
    jaba = {"kamakhya": "india", "madhu": "india", "aniket": "india", "nilesh": "india", "asha": "india"}
    kacha = [1, 2, 3, 4, 5]
    ja (kavi, *kacha, **jaba)


o='nope'
for itej in o:
    print(itej,end='')