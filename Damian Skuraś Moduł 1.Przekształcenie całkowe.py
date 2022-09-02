import time
import os
import sympy as sym
from sympy.abc import s,t,x,y,z
import numpy as np
from sympy.integrals import inverse_laplace_transform
import matplotlib.pyplot as plt
#----
print("|-------------------------------------------------------------|")
print("| Damian Skuras |---------------------------------------------|")
print("| Informatyka III rok | VI Semestr |--------------------------|")
print("| Nr.indeksu : 142873 |---------------------------------------|")
print("|-------------------------------------------------------------|")
print("| Przedmiot: Sterowanie Komputerowe i Robotyka [Labolatorium] |")
print("| Moduł 1.Przekształcenie całkowe (przypomnienie) ------------|")
print("|-------------------------------------------------------------|")
print("| Prosze przygotowac skrypt w Matlabie wyznaczajacy nastepuj. |")
print("| przeksztalcenie Laplace'a 10+5t+t^2-4t^3                    |")
print("|-------------------------------------------------------------|")
time.sleep(1)
input ("Aby przejsc dalej nacisnij klawisz ENTER:")
time.sleep(1)
print("")
# Definiujemy dane przeksztalcenie Laplace'a
n = 2
def silnia(n):
    if n > 1:
        return n * silnia(n-1)
    else:
        return 1
#n = int(input('n = '))
#print(n, '! =', silnia(n))
n1 = 3
def silnia1(n1):
    if n > 1:
        return n * silnia1(n-1)
    else:
        return 1
# -------------------------------------------
# Funkcja do przeliczenia
# G = 10+(5*t)+(t**2)-(4*t**3)
# Przekształcenie podanej funkcji do skryptu:
# -------------------------------------------
U1 = 10/s*sym.exp(-s)
U2 = 5/s**2*sym.exp(-2*s)
U3 = n/s**3*sym.exp(-3*s)
U4 = 4*n1/s**4*sym.exp(-4*s)
t=s
# Przekształcenie funkcji metodą Laplace'a:
G = U1+U2+U3-U4
print("|-------------------------------------------------------------|")
print("Wzor po przeksztalceniu:")
print()
print(G)
# Kalkulowana odpowiedz
Y1 = G*U1
Y2 = G*U2
Y3 = G*U3
Y4 = G*U4
#
print("|-------------------------------------------------------------|")
print ("Kalkulowana odpowiedz:")
print()
print(Y1)
print(Y2)
print(Y3)
print(Y4)
time.sleep(1)
print("|-------------------------------------------------------------|")
input ("Aby przejsc dalej nacisnij klawisz ENTER:")
print()
Sa = 1
ta = 1
Ga = [10/Sa+(5*ta)/(Sa**2)+n/(Sa**3)-(4*ta**3)]
print(Ga)
print()
time.sleep(1)
print("|-------------------------------------------------------------|")
input ("Aby przejsc dalej nacisnij klawisz ENTER:")
# Inverse Laplace Transform
u1 = inverse_laplace_transform(U1,s,t)
u2 = inverse_laplace_transform(U2,s,t)
u3 = inverse_laplace_transform(U3,s,t)
u4 = inverse_laplace_transform(U4,s,t)
y1 = inverse_laplace_transform(Y1,s,t)
y2 = inverse_laplace_transform(Y2,s,t)
y3 = inverse_laplace_transform(Y3,s,t)
y4 = inverse_laplace_transform(Y4,s,t)
print('y1')
print(y1)
#generate data for plot
tm = np.linspace(0,8,100)
us = np.zeros(len(tm))
ys = np.zeros(len(tm))
# substytuty numeryczne dla wartosci u i y
for u in [u1,u2,u3,u4]:
    for i in range(len(tm)):
        us[i] += u.subs(t,tm[i])
for y in [y1,y2,y3,y4]:
    for i in range(len(tm)):
        ys[i] += y.subs(t,tm[i])
# plot results
plt.figure()
plt.plot(tm,us,label='u(t)')
plt.plot(tm,ys,label='y(t)')
plt.legend()
plt.xlabel('Time')
