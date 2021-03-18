import time
k = 0
initial=time.time()
while (k < 45):
    print ("This is harry bhai")
    time.sleep (0.01)
    k += 1
print ("While loop ran in", time.time () - initial, "Seconds")

initial2 = time.time ()
for i in range (45):
    print ("This is harry bhai")
print ("For loop ran in", time.time () - initial2, "Seconds")

localtime = time.asctime(time.localtime(time.time()))#time.asctime coverts time into a time which can be understood by us
print(localtime)
print(time.time())
time.sleep(10)
print("tsasa")

