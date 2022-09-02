import random
import time
import sys
print("|--------------------------|")
print("| Damian Skuras            |")
print("| A.H.E Informatyka III rok|")
print("| VI Semestr | Nr:142873   |")
print("|--------------------------|")
time.sleep(1)
number1 = random.randint(1, 100)
print("First number is %d" % (number1))
counter = 1
number2 = random.randint(1, 100)
#-
while number1 != number2:
    counter += 1
    number2 = random.randint(1, 100)
    print(counter, number2)

print("\n")
print("Number of attempts", counter, number1)
time.sleep(1)
print()
print("|--------------------------|")
input("Aby zakonczyc nacisnij klaiwsz enter:")
time.sleep(3)
sys.exit()
