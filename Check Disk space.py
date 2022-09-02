import time
import sys
print("|--------------------------|")
print("| Damian Skuras            |")
print("| A.H.E Informatyka III rok|")
print("| VI Semestr | Nr:142873   |")
print("|--------------------------|")
time.sleep(1)
#------------------------------------------------
diskSize = 100
diskSizeUsed = 90
fileSize = 15

if fileSize <= (diskSize - diskSizeUsed):
    print("File can be downoladed")
else:
    print("No space on disk")
time.sleep(1)
print("|--------------------------|")
input("Aby zakonczyc nacisnij klaiwsz enter:")
time.sleep(3)
sys.exit()
#---
