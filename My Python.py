import time
print("Program drukujący napis Python")
print("------------------------")
my_string = "Python"
x =0

for i in my_string:
    x = x+1
    print(my_string[0:x])

for i in my_string:
    x = x-1
    print(my_string[0:x])
print("------------------------")
print ("Dziękuje za uwagę :) ")

localtime = time.asctime( time.localtime(time.time()) )
print("------------------------")
print(localtime)
print("------------------------")
input("Press Enter to continue...")
#--
import calendar
#-
cal = calendar.month(2022, 1)
print ("Here is the calendar:")
print (cal)
input("Press Enter to continue...")
