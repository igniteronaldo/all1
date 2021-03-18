zuckerberg=["chowmin","pizza" ,"sabbooon","gamu"]
print(type(zuckerberg))
print(zuckerberg)
for re,x in enumerate(zuckerberg):
    if re%1 == 0:#sab ke liye same hi karan hoga toh ache se samaj lo bhaiyaji.
        print(x) #kitne ka difference chahiye strings ke bech ka jaie 1,2,3,4 ,matlab x yaha par.
                 #yaha par hum sabhi ke  pyare        re ka value 0 default set hota hai.
                 # change karne ke lye re ka value ek variable banao aur re ka apna  value daldo.
                 #aur agar yeh sab 0 hota hai module (yani ki percentage [python me,abhi bhi nahi samjha toh operator module dekh lo# )
                 #toh phir yeh ab ekdam simply print karde ga x ko jaise yaha par 1 ka difference le kar sabhi ko priint karega agar == 0 or zero hota hai toh.
    elif re%3 == 0:
         print(x)
    elif re % 2 == 0:
         print(x)
    elif re % 4 == 0:
         print(x)
    break

elon=["musk","harry","tiwari"]
for gam,kam in enumerate(elon):
    if gam%1==0:
        print(kam)
        gam=gam+2
    if gam %  4 ==0:
        print(kam)