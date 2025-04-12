import time

curr = time.localtime()
print("local time is : ",curr)

hours_minutes = time.strftime("%H:",curr)
only_hrs = int(hours_minutes[0:len(hours_minutes)-1])
print("time in hours and minutes is: ",only_hrs)
# only_hrs = 22
if(0<only_hrs<12):
    print("Good Morning")
elif(12<=only_hrs<17):
    print("Good afternoon")
elif(17<=only_hrs<=20):
    print("Good evening")
else:
    print("Good night")