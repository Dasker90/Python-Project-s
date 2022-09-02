import time
import math
import sys
import numpy as np
# --- Biblioteki
print("--------------------------------")
print("Damian Skuraś")
print("Informatyka III rok | VI Semestr")
print("Moduł 6. Zera i bieguny, postacie kanoniczne")
print("--------------------------------")
time.sleep(2)
input("Aby przejść dalej naciśnij klawisz ENTER:")
time.sleep(2)
A = (1/2)
print()
print("--------------------------------")
print ("Macierz A wygląda następujaco:",A)
WierszA=[-3,-1,1]
WierszB=[1,-5,-1]
WierszC=[2,-2,-4]
a = np.array (WierszA)
b = np.array (WierszB)
c = np.array (WierszC)
print("--------------------------------")
print ("Macierz P wygląda następujaco:")
print(a)
print(b)
print(c)
time.sleep(2)
print()
print("--------------------------------")
print("Obliczona macierz P przekształcona w macierz A wygląda następująco:")
print("--------------------------------")
# Mnożenie macierz P*A ---------------------------------------------
wynik1 = [WierszA[0]*A,WierszA[1]*A,WierszA[2]*A]
wynik2 = [WierszB[0]*A,WierszB[1]*A,WierszB[2]*A]
wynik3 = [WierszC[0]*A,WierszC[1]*A,WierszC[2]*A]
d = np.array (wynik1)
e = np.array (wynik2)
f = np.array (wynik3)
print(d)
print(e)
print(f)
# - Warunki do liczenia macierzy w postać diagonalną:
# Kolumna A1 ------------------------------------------------------
if wierszA[0] >1:
    return
elif wierszA[0] = 0:
    print ("Wartość 1x1 kolumny równa 0 , równanie nie diagonalne !")
    break
else:
    print ("Równanie sprzeczne !")
# Kolumna A2 ------------------------------------------------------
if wierszA[1] >1:
    return
elif wierszA[1] = 0:
    print ("Wartość 2x1 kolumny równa 0 , równanie nie diagonalne !")
    break
else:
    print ("Równanie sprzeczne !")
# Kolumna A3 ------------------------------------------------------
if wierszA[2] >1:
    return
elif wierszA[2] = 0:
    print ("Wartość 3x1 kolumny równa 0 , równanie nie diagonalne !")
    break
else:
    print ("Równanie sprzeczne !")
# Kolumna B1 ------------------------------------------------------
if wierszB[0] >1:
    return
elif wierszB[0] = 0:
    print ("Wartość 2x1 kolumny równa 0 , równanie nie diagonalne !")
    break
else:
    print ("Równanie sprzeczne !")
# Kolumna B2 ------------------------------------------------------
if wierszB[1] >1:
    return
elif wierszB[1] = 0:
    print ("Wartość 2x2 kolumny równa 0 , równanie nie diagonalne !")
    break
else:
    print ("Równanie sprzeczne !")
# Kolumna B3 ------------------------------------------------------
if wierszB[2] >1:
    return
elif wierszB[2] = 0:
    print ("Wartość 2x3 kolumny równa 0 , równanie nie diagonalne !")
    break
else:
    print ("Równanie sprzeczne !")
# Kolumna C1 ------------------------------------------------------
if wierszC[0] >1:
    return
elif wierszC[0] = 0:
    print ("Wartość 3x1 kolumny równa 0 , równanie nie diagonalne !")
    break
else:
    print ("Równanie sprzeczne !")
# Kolumna C2 ------------------------------------------------------
if wierszC[1] >1:
    return
elif wierszC[1] = 0:
    print ("Wartość 3x2 kolumny równa 0 , równanie nie diagonalne !")
    break
else:
    print ("Równanie sprzeczne !")
# Kolumna C3 ------------------------------------------------------
if wierszC[2] >1:
    return
elif wierszC[2] = 0:
    print ("Wartość 3x3 kolumny równa 0 , równanie nie diagonalne !")
    break
else:
    print ("Równanie sprzeczne !")
# Postac diagonalna (bibliotek pyth do obliczenia)
Diag = mathsqrt([d,e,f])
if Diag == True:
    print ("Macierz ma postać diagonalną !")
    print (Diag)
    break
elif Diag == False:
    print ("Macierz nie ma postaci diagonalnej")
    break
    sys.exit(1)
# -----------------------------------------------------------------
print("Macierz A nie ma postaci diagonalne , ponieważ elementy leżące poza przekątną nie są równe 0,")
print("--------------------------------")
time.sleep(2)
input("Aby wyjść z programu naciśnij klawisz ENTER:")
sys.exit(2)
