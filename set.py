bihari =  {"tiwari","waah kya baat hai"}

bihari.remove("tiwari")
print(bihari)
print(type(bihari))
bihari.add("neymar")
print(bihari)
print(bihari.union({1,2}))
#does not accept duplicate elements
#they are unordered
#it is represented in {} and is written like this
a= {"waah ji","badhiya","tiwari","waah kya baat hai"}
print(type(a))
#samjhe bhaiyaji
#to create empty set
b =  {"this is a set now and not a dictiooooooookooooooooooooooooooo"}
print(type(b))
#samje bhaiyaji
print(id(b))
print(b,a)
#intersection mane jo dono me samil hota hai
#samjha bhaiyaji
print(bihari.intersection({"neymar"}))
print(min(bihari))
print(max(bihari))
print(len(bihari))
print(bihari.difference(a))
print(bihari.isdisjoint(a))
c={"india"}
print(type(c))
print(bihari.isdisjoint(b))
#isdisjoint tab hi true dega jab kuch bhi commmon nahi hoga.


