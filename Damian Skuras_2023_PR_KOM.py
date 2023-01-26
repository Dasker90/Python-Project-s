import time             #biblioteka czasu        
import sys
import random
import matplotlib.pyplot as plt
import numpy as np
from sys import maxsize
from random import randint
print("---------------------------------------------")
print("v: 0.1 z 12.02.2022 r.")
print("---------------------------------------------")
print("Start: %s" % time.ctime())
print("---------------------------------------------")
time.sleep(1)
print("")
print("---------------------------------------------")
print("Akademia Humanistyczno-Ekonoiczna w Łodzi")
print("---------------------------------------------")
print("Wydział : Informatyki , Zarządzania i Transportu")
print("Damian Skuras")
print("Kierunek:Informatyka III rok , VII semestr")
print("Numer Indeksu:142873")
print("---------------------------------------------")
print("Przedmiot: Metody optymalizacji [LABOLATORIUM]-[ZADANIE 7]")
print("Nazwa: Problem Komiwojazera ")
print("---------------------------------------------")
time.sleep(1)
#------------------------------
# Wspolrzedne klientow na terenie miasta Sieradz
a1 = random.randint(-1,1)  #Pkt startowy (BAZA)
b1 = random.randint(0,3)
c1 = random.randint(1,8)
d1 = random.randint(1,8)
e1 = random.randint(1,8)
f1 = random.randint(1,8)
g1 = random.randint(1,8)
h1 = random.randint(1,8)
i1 = random.randint(1,8)
j1 = random.randint(1,8)
k1 = random.randint(1,8)
l1 = random.randint(6,9)
a2 = random.randint(-1,2) #Pkt startowy (BAZA)
b2 = random.randint(1,8)
c2 = random.randint(1,8)
d2 = random.randint(1,8)
e2 = random.randint(3,8)
f2 = random.randint(1,8)
g2 = random.randint(4,8)
h2 = random.randint(1,8)
i2 = random.randint(1,8)
j2 = random.randint(1,8)
k2 = random.randint(1,8)
l2 = random.randint(7,9)
#------------------------------
x = [a1,b1,c1,d1,e1,f1,g1,h1,i1,j1,k1,l1]
y = [a2,b2,c2,d2,e2,f2,g2,h2,i2,j2,k2,l2]
# Ploty wspolzedne na wykres
plt.plot(x, y, color='red', linestyle='dashed', linewidth = 2,marker='X', markerfacecolor='black',markersize=10)
plt.ylim(-1,10)
plt.xlim(-1,10)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Problem komiwojazera na przykladzie miasta Sieradz')
plt.show()
#------------------------------
time.sleep(3)
input("Aby wyjsc z programu nacisnij klawisz [ENTER]")
sys.exit()