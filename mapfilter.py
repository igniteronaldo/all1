

#numbers=["2","3","4","5"]
#print(int(numbers))  #error       milore bhai.
#numbers[3]=numbers[2]+1 #error       milore bhai.
#numbers[3]=numbers[3]+1 #error       milore bhai.



#ye hai normal life.

#for item in range(len(numbers)):
   # numbers[item]= int(numbers[item])

#numbers[3]=numbers[3] + 5
#print(numbers[1])
#print(numbers[3])

                                 #map map map map map map map map map map
#ab aate hai hamare pyare      pyare map function mein:just type map to actiavte
#map kya karta hai ki yeh      na tumhare dwara diye gaye numbers ke sath woh karta hai jo tum ise bolte ho
#SAMJHE BABUJI ,bas itna        hi.


#rasi=(map(int,numbers))
#print(rasi)#bahut ajib hai.
#kaq=list(map(int,numbers))
#print(kaq)#ajib nahi hai       yeh utna kyun ki   proper implementation of map

#num=["2","3","4","5","6",       "7"]
#ha=list(map(int,num))
#print(ha)


#kuch naya ab yaha se,          niche  toh dekho    zara.
#zam=["2","3","4","5","6",       "7"]
#ha=list(map(int,zam))
#square=list(map(lambda x:x*x,ha))
#print(square)
#cube=list(map( lambda z:z**z,ha))
#print(cube)
#remener that * mean multiply
#and ** means "to the power".


#practice of map
#def square(a):
#    return a*a
#def cube(b):
#    return b*b*b

#func= square,cube
#for i in range(5):
#    lal=list(map(lambda     x:x(i),func))
#    print(lal)


                    # filter   filter filter filter filter filter filter filter

#basic of filter function and   to use filter       type filter


#list1=["2","3","4","5","6",7]
#ra = list(map(int,list1))

#def is_greaterr_than(a):
#    return a>5

#junior=list(filter(is_greaterr_than,ra))
#print(junior)




            # reduce reduce reduce reduce reduce reduce reduce reduce reduce

from functools import reduce
from  _functools import reduce




list1=["2","3","4","5","6",7]
ra = list(map(int,list1))

na=0
# THIS IS NORMAL LIFE.
for i in ra:
    na= na + i
print("YEH HAI NORMAL LIFE:",na,"VERY DISCIPLINED.")


# THIS IS MENTOS LIFE.

ra.append(2)#to add 2 i         used append .          because i forget to add 2 again.
biden=reduce(lambda          e,y:e+y,ra)
riden=reduce(lambda          e,y:e*y,ra)#it will    multiply first 2 with 3 then product of 2 and 3 with 4 and son on.
print("YAHI TOH HAI MENTOS     LIFE",biden,"VERY UNDISCIPLINED")
print("YAHI TOH HAI MENTOS     LIFE",riden,"VERY UNDISCIPLINED")


















