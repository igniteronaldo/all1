tiwari={}
print(type(tiwari))
tiwari1={"baba":"salad",
         "boss":"eats",
         "papa":"chicken dinner",
         "madhu":{"b":"breakfast","l":"lunch","d":"dinner"}}
print(tiwari1)
print(tiwari1["baba"])
print(tiwari1.items())
tiwari1.get("baba")
print(tiwari1)
print(tiwari1.get("baba"))
tiwari1["aniket"]="only one"
print(tiwari1)
tiwari1.update({"mansi":"jejdd"})
print(tiwari1)
print(tiwari1["madhu"])
print(tiwari1["madhu"]["b"])
print(tiwari1["madhu"].keys())
print(tiwari1["madhu"].items())
tiwari2=tiwari1.copy()
del tiwari2["madhu"]
print(tiwari2)
print(tiwari1)

