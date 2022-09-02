#-----------------------------------------------------------------------|
import time             #biblioteka czasu
import datetime
import sys
import random
from random import randint
#------------------------------------------------------------------------
print("---------------------------------------------")
print("v: 0.1 z 12.02.2022 r.")
print("---------------------------------------------")
print("Start: %s" % time.ctime())
print("---------------------------------------------")
haslo=input("Podaj Haslo do zalogowania:")
if haslo=='qweas':
    print("---------------------------------------------")
    print("Zalogowales sie poprawnie !")
    print("---------------------------------------------")
    time.sleep(3)
#-
    else:
    print("Bledne Haslo!")
    time.sleep(3)
    sys.exit()
#------------------------------------------------------------------------
# Autor -----------------------------------------------------------------
#------------------------------------------------------------------------
print("Akademia Humanistyczno-Ekonoiczna w Łodzi")
print("---------------------------------------------")
print("Wydział : Informatyki , Zarządzania i Transportu")
print("Damian Skuras")
print("Kierunek:Informatyka III rok , V semestr")
print("Numer Indeksu:142873")
print("---------------------------------------------")
print("Przedmiot: Podstawy Programowania [LABOLATORIUM]-[ZADANIE 5]")
print("Nazwa: Symulacja Lini MPK-SIERADZ ")
print("---------------------------------------------")
time.sleep(3)
#---------------------|
# Dane do programu , który bedzie losowo dobierał kierowcę do danego autobusu.
#---------------------|
Kierowca = (["Bogdan","Robert","Arkadiusz","Piotr","Damian","Volodia"])
ID_Kierowcy =(["PL101","PL102","PL103","PL104","PL105","UKR001"])
#---------------------|
# print (random.choice(Kierowca))
# print (random.choice(ID_Kierowcy))
#---------------------|
input("Aby przejsc dalej nacisnij klawisz [ENTER]")
time.sleep(3)
print()
print()
print("|-------------------------------------------------------|")
print("|--------------    Model Pojazdu:      -----------------|")
print("|-------------------------------------------------------|")
print("""
|-------------------------------------------------------|
| Marka:                 Solaris Urbino 15H.            |
| Kolor:                 Zielony.                       |
| Max.liczba.pasazerow : 35 osob.                       |
| Rok produkcji:         2012 rok.                      |
| Paliwo:                DIESEL.                        |
| Numer rejestracyjny:   ESI 301CL.                     |""")
#print("| Przebieg pojazdu:__km z dnia","%s |" % time.ctime())
print("|-------------------------------------------------------|")
# Rozkład jazdy lini autobusowej w Sieradzu.
input("Aby przejsc dalej nacisnij klawisz [ENTER]")
time.sleep(3)
print()
print()
#----------------------------------------------------------------
# Rozkład Lini Nr 4 w Sieradzu : Kurs pomiedzy przystankami
#----------------------------------------------------------------
print("""
|------------------------------------------------------------|
|                      LINIA NR:4                            |        
|------------------------------------------------------------|
|| LP |            Ulica              |   OZN     | Dod.Inf ||
|------------------------------------------------------------|
| 1   | Mickiewicza_Petla             | 1 3 5 t   | Start b  |
| 2   | Wojska Polskiego              | 1   5     |          |
| 3   | Wojska Polskiego_Rondo        | 1 3 5 t a |          | 
| 4   | Jana Pawla II PKS             | 1 3 5 t   |          |
| 5   | Jana Pawla II Bartek          | 1   5 t   |          |
| 6   | Broniewskiego I               | 1 3 5 t   |          |
| 7   | Krakowskie Przedmiescie_Petla | 1 3 5 t   | Koniec b |
|------------------------------------------------------------|
|1 - Kursuje od Pn do SB.                                    |
|3 - Kursuje od SB do ND.                                    |
|5 - Kursuje w dni Swiateczne.                               |
|t - Kursuje w wakacje letnie.                               |
|w - Nie kursuje w wakacje letnie.                           |
|a - Nie kursuje w dni Swiateczne.                           |
|b - Przerwa dla kierowcy.                                   |
|------------------------------------------------------------|
""")
time.sleep(1)
time.sleep(1)
input("Aby przejsc dalej nacisnij klawisz [ENTER]")
time.sleep(3)
print()
print()
print()
print()
print()
print()
#---- Symulacja -----------------------------------------------------------|
Paliwo = (random.randint(29,51))              # Średnie spalanie autobusu.
Zbiornik_Autobusu = (500)                     # pojemnosc w litach (L).
Liczba_Wsiadajacych = random.randint(0,16)    # Wsiadający pasażerowie.
Liczba_Wysiadajacych = random.randint(0,16)   # Wysiadający pasażerowie.
Stacje = (random.randint(0,10))               # Odległość pomiędzy stacjami.
# print (random.uniform(0,16)) CZAS
# print (random.uniform(0,16)) ODległosc
# print (random.uniform(0,2))
#---------------------|
# -| Uruchomienie Pojazdu |-
print("---------------------------------------------")
print("Wloz karte kierowcy! ")
time.sleep(3)
print("Trwa uruchomienie silnika:")
time.sleep(3)
print("Silnik uruchomiony!")
print("---------------------------------------------")
time.sleep(3)
#---------------------|
# -| Identyfikacja kierowcy |-
print()
print("---------------------------------------------")
print("MPK SIERADZ |                                ")
print("---------------------------------------------")
print("Imie Kierowcy:")
print (random.choice(Kierowca))
print("ID Kierowcy:")
print (random.choice(ID_Kierowcy))
print("---------------------------------------------")
#---------------------|
time.sleep(3)
print()
print()
print("Autobus ruszyl!")
time.sleep(3)
print()
print()
import datetime
now=datetime.datetime.now()
t=now.strftime('%H:%M:%S')
print("Autobus zatrzymal sie na przystanku nr:1 !")
time.sleep(3)
input("Aby przejsc dalej nacisnij klawisz [ENTER]")
time.sleep(3)
#------------------------------------------------------------------------
# 1 przystanek autobusowy
#------------------------------------------------------------------------
print("|------------------------------------------------------------|")
print("|                      LINIA NR:4   Przystanek: 1            |")
print("|------------------------------------------------------------|")
print("| Stacja Biezaca    | Stacja nastepna  |                     |")
print("|------------------------------------------------------------|")
print("| Mickiewicza_Petla | Wojska Polskiego | PRZYJAZD -> ODJAZD  |")
print("|------------------------------------------------------------|")
print("| Przyjazd:",(t))
print("| Do autobusu wsiadlo:",(Liczba_Wsiadajacych),"pasazerow","  |")
print("|------------------------------------------------------------|")
input("Wcisnij ENTER:")
print("")
time.sleep(3)
V = random.randrange(10,52)
V25 = random.randrange(10,52)
V50 = random.randrange(10,52)
V75 = random.randrange(10,52)
V100 = random.randrange(10,52)
print("Zamknij drzwi boczne autobusu!")
input("Wcisnij klawisz ENTER:")
time.sleep(3)
print("Autobus wyruszył na droge !")
time.sleep(3)
#------------------------------------------------------------------------
# Symulacja czasu przebycia autobusu pomiedzy stacjami.
#------------------------------------------------------------------------
print("|------------------------------------------------------------|")
print("[Poprzednia stacja]-------[Stacja Nastepna] |",V*0,"km/h |")
time.sleep(3)
print("[Poprzednia stacja]-[X]---[Stacja Nastepna] |",V25,"km/h |")
time.sleep(3)
print("[Poprzednia stacja]--[X]--[Stacja Nastepna] |",V50,"km/h |")
time.sleep(3)
print("[Poprzednia stacja]---[X]-[Stacja Nastepna] |",V75,"km/h |")
time.sleep(3)
print("[Poprzednia stacja]----[X][Stacja Nastepna] |",V100,"km/h |")
time.sleep(3)
print("[Poprzednia stacja]-------[Stacja Nastepna] |",V*0,"km/h |")
print("|------------------------------------------------------------|")
time.sleep(3)
print("")
print("Autobus dojechał do drugiej stacji !")
#------------------------------------------------------------------------
# 2 przystanek autobusowy
#------------------------------------------------------------------------
time.sleep(3)
print("")
BLiczba_Wsiadajacych = random.randint(0,16)
import datetime
now=datetime.datetime.now()
a=now.strftime('%H:%M:%S')
print("|------------------------------------------------------------|")
print("|                      LINIA NR:4     Przystanek: 2          |")
print("|------------------------------------------------------------|")
print("| Stacja Poprzednia | Stacja biezaca   | Stacja Nastepma     |")
print("|------------------------------------------------------------|")
print("| Mickiewicza_Petla | Wojska Polskiego | Wojska Polskiego R. |")
print("|------------------------------------------------------------|")
print("| Przyjazd:",(a))
print("| Z autobusu wysiadlo:",(Liczba_Wsiadajacych),"pasazerow")
print("| Do autobusu wysiadlo:",(BLiczba_Wsiadajacych),"pasazerow")
print("|------------------------------------------------------------|")
AV = random.randrange(10,52)
AV25 = random.randrange(10,52)
AV50 = random.randrange(10,52)
AV75 = random.randrange(10,52)
AV100 = random.randrange(10,52)
input("Wcisnij klawisz ENTER:")
time.sleep(3)
print("Zamknij drzwi boczne autobusu!")
input("Wcisnij klawisz ENTER:")
time.sleep(3)
print("Autobus wyruszył na droge !")
time.sleep(3)
print("|------------------------------------------------------------|")
print("[Poprzednia stacja]-------[Stacja Nastepna] |",AV*0,"km/h |")
time.sleep(3)
print("[Poprzednia stacja]-[X]---[Stacja Nastepna] |",AV25,"km/h |")
time.sleep(3)
print("[Poprzednia stacja]--[X]--[Stacja Nastepna] |",AV50,"km/h |")
time.sleep(3)
print("[Poprzednia stacja]---[X]-[Stacja Nastepna] |",AV75,"km/h |")
time.sleep(3)
print("[Poprzednia stacja]----[X][Stacja Nastepna] |",AV100,"km/h |")
time.sleep(3)
print("[Poprzednia stacja]-------[Stacja Nastepna] |",AV*0,"km/h |")
print("|------------------------------------------------------------|")
print("")
print("Autobus dojechał do trzeciej stacji !")
print("")
#------------------------------------------------------------------------
# 3 przystanek autobusowy
#------------------------------------------------------------------------
time.sleep(3)
import datetime
now=datetime.datetime.now()
b=now.strftime('%H:%M:%S')
CLiczba_Wsiadajacych = random.randint(0,16)
print("|------------------------------------------------------------|")
print("|                      LINIA NR:4   Przystanek: 3            |")
print("|------------------------------------------------------------|")
print("| Stacja Poprzednia | Stacja biezaca      | Stacja Nastepma  |")
print("|------------------------------------------------------------|")
print("| Wojska Polskiego  | Wojska Polskiego R. | Jana PawłaII PKS |")
print("|------------------------------------------------------------|")
print("| Przyjazd:",(b))
print("| Z autobusu wysiadlo:",(BLiczba_Wsiadajacych),"pasazerow")
print("| Do autobusu wysiadlo:",(CLiczba_Wsiadajacych),"pasazerow")
print("|------------------------------------------------------------|")
time.sleep(3)
input("Wcisnij klawisz ENTER:")
time.sleep(3)
print("Zamknij drzwi boczne autobusu!")
input("Wcisnij klawisz ENTER:")
time.sleep(3)
print("Autobus wyruszył na droge !")
time.sleep(3)
BV = random.randrange(10,52)
BV25 = random.randrange(10,52)
BV50 = random.randrange(10,52)
BV75 = random.randrange(10,52)
BV100 = random.randrange(10,52)
print("|------------------------------------------------------------|")
print("[Poprzednia stacja]-------[Stacja Nastepna] |",BV*0,"km/h |")
time.sleep(3)
print("[Poprzednia stacja]-[X]---[Stacja Nastepna] |",BV25,"km/h |")
time.sleep(3)
print("[Poprzednia stacja]--[X]--[Stacja Nastepna] |",BV50,"km/h |")
time.sleep(3)
print("[Poprzednia stacja]---[X]-[Stacja Nastepna] |",BV75,"km/h |")
time.sleep(3)
print("[Poprzednia stacja]----[X][Stacja Nastepna] |",BV100,"km/h |")
time.sleep(3)
print("[Poprzednia stacja]-------[Stacja Nastepna] |",BV*0,"km/h |")
print("|------------------------------------------------------------|")
print("")
print("Autobus dojechał do czwartej stacji !")
print("")
#-----------------------------------------------------------------------
# 4 przystanek autobusowy
#------------------------------------------------------------------------
time.sleep(3)
import datetime
now=datetime.datetime.now()
c=now.strftime('%H:%M:%S')
DLiczba_Wsiadajacych = random.randint(0,16)
print("|------------------------------------------------------------|")
print("|                      LINIA NR:4     Przystanek: 4          |")
print("|------------------------------------------------------------|")
print("| Stacja Poprzednia | Stacja biezaca      | Stacja Nastepma  |")
print("|------------------------------------------------------------|")
print("| Wojska Polskiego  | Wojska Polskiego R. | Jana PawłaII PKS |")
print("|------------------------------------------------------------|")
print("| Przyjazd:",(c))
print("| Z autobusu wysiadlo:",(CLiczba_Wsiadajacych),"pasazerow")
print("| Do autobusu wysiadlo:",(DLiczba_Wsiadajacych),"pasazerow")
print("|------------------------------------------------------------|")
time.sleep(3)
input("Wcisnij klawisz ENTER:")
time.sleep(3)
print("Zamknij drzwi boczne autobusu!")
input("Wcisnij klawisz ENTER:")
time.sleep(3)
print("Autobus wyruszył na droge !")
time.sleep(3)
DV = random.randrange(10,52)
DV25 = random.randrange(10,52)
DV50 = random.randrange(10,52)
DV75 = random.randrange(10,52)
DV100 = random.randrange(10,52)
# Symulacja prędkości autobusu
print("|------------------------------------------------------------|")
print("[Poprzednia stacja]-------[Stacja Nastepna] |",DV*0,"km/h |")
time.sleep(3)
print("[Poprzednia stacja]-[X]---[Stacja Nastepna] |",DV25,"km/h |")
time.sleep(3)
print("[Poprzednia stacja]--[X]--[Stacja Nastepna] |",DV50,"km/h |")
time.sleep(3)
print("[Poprzednia stacja]---[X]-[Stacja Nastepna] |",DV75,"km/h |")
time.sleep(3)
print("[Poprzednia stacja]----[X][Stacja Nastepna] |",DV100,"km/h |")
time.sleep(3)
print("[Poprzednia stacja]-------[Stacja Nastepna] |",DV*0,"km/h |")
print("|------------------------------------------------------------|")
#------------------------------------------------------------------------
# 5 przystanek autobuspwy
#------------------------------------------------------------------------
time.sleep(3)
import datetime
now=datetime.datetime.now()
e=now.strftime('%H:%M:%S')
ELiczba_Wsiadajacych = random.randint(0,16)
print()
print("|------------------------------------------------------------|")
print("|                      LINIA NR:4   Przystanek: 5            |")
print("|------------------------------------------------------------|")
print("| Stacja Poprzednia | Stacja biezaca      | Stacja Nastepma  |")
print("|------------------------------------------------------------|")
print("| W.P_Rondo         | J.P II PKS          | J.P II Bartek    |")
print("|------------------------------------------------------------|")
print("| Przyjazd:",(e))
print("| Z autobusu wysiadlo:",(DLiczba_Wsiadajacych),"pasazerow")
print("| Do autobusu wysiadlo:",(ELiczba_Wsiadajacych),"pasazerow")
print("|------------------------------------------------------------|")
time.sleep(3)
input("Wcisnij klawisz ENTER:")
time.sleep(3)
print("Zamknij drzwi boczne autobusu!")
input("Wcisnij klawisz ENTER:")
time.sleep(3)
print("Autobus wyruszył na droge !")
time.sleep(3)
EV = random.randrange(10,52)
EV25 = random.randrange(10,52)
EV50 = random.randrange(10,52)
EV75 = random.randrange(10,52)
EV100 = random.randrange(10,52)
print()
print("|------------------------------------------------------------|")
print("[Poprzednia stacja]-------[Stacja Nastepna] |",EV*0,"km/h |")
time.sleep(3)
print("[Poprzednia stacja]-[X]---[Stacja Nastepna] |",EV25,"km/h |")
time.sleep(3)
print("[Poprzednia stacja]--[X]--[Stacja Nastepna] |",EV50,"km/h |")
time.sleep(3)
print("[Poprzednia stacja]---[X]-[Stacja Nastepna] |",EV75,"km/h |")
time.sleep(3)
print("[Poprzednia stacja]----[X][Stacja Nastepna] |",EV100,"km/h |")
time.sleep(3)
print("[Poprzednia stacja]-------[Stacja Nastepna] |",EV*0,"km/h |")
print("|------------------------------------------------------------|")
#------------------------------------------------------------------------
# 6 przystanek autobusowy
#------------------------------------------------------------------------
time.sleep(3)
import datetime
now=datetime.datetime.now()
f=now.strftime('%H:%M:%S')
FLiczba_Wsiadajacych = random.randint(0,16)
time.sleep(3)
print("Autobus wyruszył na droge !")
time.sleep(3)
print("|------------------------------------------------------------|")
print("|                      LINIA NR:4    Przystanek: 6           |")
print("|------------------------------------------------------------|")
print("| Stacja Poprzednia | Stacja biezaca      | Stacja Nastepma  |")
print("|------------------------------------------------------------|")
print("| J.P II PKS        | J.P II Bartek       | Broniewskiego I  |")
print("|------------------------------------------------------------|")
print("| Przyjazd:",(f))
print("| Z autobusu wysiadlo:",(ELiczba_Wsiadajacych),"pasazerow")
print("| Do autobusu wysiadlo:",(FLiczba_Wsiadajacych),"pasazerow")
print("|------------------------------------------------------------|")
time.sleep(3)
input("Wcisnij klawisz ENTER:")
time.sleep(3)
print("Zamknij drzwi boczne autobusu!")
input("Wcisnij klawisz ENTER:")
time.sleep(3)
print("Autobus wyruszył na droge !")
time.sleep(3)
FV = random.randrange(10,52)
FV25 = random.randrange(10,52)
FV50 = random.randrange(10,52)
FV75 = random.randrange(10,52)
FV100 = random.randrange(10,52)
print()
print("|------------------------------------------------------------|")
print("[Poprzednia stacja]-------[Stacja Nastepna] |",FV*0,"km/h |")
time.sleep(3)
print("[Poprzednia stacja]-[X]---[Stacja Nastepna] |",FV25,"km/h |")
time.sleep(3)
print("[Poprzednia stacja]--[X]--[Stacja Nastepna] |",FV50,"km/h |")
time.sleep(3)
print("[Poprzednia stacja]---[X]-[Stacja Nastepna] |",FV75,"km/h |")
time.sleep(3)
print("[Poprzednia stacja]----[X][Stacja Nastepna] |",FV100,"km/h |")
time.sleep(3)
print("[Poprzednia stacja]-------[Stacja Nastepna] |",FV*0,"km/h |")
print("|------------------------------------------------------------|")
print()
#------------------------------------------------------------------------
# 7 przystanek autobusowy
#------------------------------------------------------------------------
time.sleep(3)
import datetime
now=datetime.datetime.now()
g=now.strftime('%H:%M:%S')
GLiczba_Wsiadajacych = random.randint(0,16)
input("Wcisnij klawisz ENTER:")
time.sleep(3)
print("|------------------------------------------------------------|")
print("|                      LINIA NR:4        Stacja: 7           |")
print("|------------------------------------------------------------|")
print("| Stacja Poprzednia | Stacja biezaca      | Stacja Nastepma  |")
print("|------------------------------------------------------------|")
print("| J.P II Bartek | Broniewskeigo  | Krakowskie Przedmiescie_Petla  |")
print("|------------------------------------------------------------|")
print("| Przyjazd:",(g))
print("| Z autobusu wysiadlo:",(FLiczba_Wsiadajacych),"pasazerow")
print("| Do autobusu wysiadlo:",(GLiczba_Wsiadajacych),"pasazerow")
print("|------------------------------------------------------------|")
print()
time.sleep(3)
input("Wcisnij klawisz ENTER:")
time.sleep(3)
print("Zamknij drzwi boczne autobusu!")
input("Wcisnij klawisz ENTER:")
time.sleep(3)
print("Autobus wyruszył na droge !")
time.sleep(3)
GV = random.randrange(10,52)
GV25 = random.randrange(10,52)
GV50 = random.randrange(10,52)
GV75 = random.randrange(10,52)
GV100 = random.randrange(10,52)
print("|------------------------------------------------------------|")
print("[Poprzednia stacja]-------[Stacja Nastepna] |",GV*0,"km/h |")
time.sleep(3)
print("[Poprzednia stacja]-[X]---[Stacja Nastepna] |",GV25,"km/h |")
time.sleep(3)
print("[Poprzednia stacja]--[X]--[Stacja Nastepna] |",GV50,"km/h |")
time.sleep(3)
print("[Poprzednia stacja]---[X]-[Stacja Nastepna] |",GV75,"km/h |")
time.sleep(3)
print("[Poprzednia stacja]----[X][Stacja Nastepna] |",GV100,"km/h |")
time.sleep(3)
print("[Poprzednia stacja]-------[Stacja Nastepna] |",GV*0,"km/h |")
print("|------------------------------------------------------------|")
print()
#------------------------------------------------------------------------
# 8 przystanek autobusowy [koncowy]
#------------------------------------------------------------------------
time.sleep(3)
import datetime
now=datetime.datetime.now()
h=now.strftime('%H:%M:%S')
print("Autobus dotarł do koncowej stacji !")
time.sleep(3)
print("Autobus wyruszył na droge !")
time.sleep(3)
print()
print("|------------------------------------------------------------|")
print("|                      LINIA NR:4    Stacja: koncowa         |")
print("|------------------------------------------------------------|")
print("| Stacja Poprzednia | Stacja biezaca      | Stacja Nastepma  |")
print("|------------------------------------------------------------|")
print("| Broniewskeigo     | Krakowskie Przedmiescie_Petla | [x] [b]      |")
print("|------------------------------------------------------------|")
print("| Przyjazd:",(h))
print("| Z autobusu wysiadlo:",(GLiczba_Wsiadajacych),"pasazerow")
print("| Do autobusu wysiadlo:",(GLiczba_Wsiadajacych*0),"pasazerow")
print("|------------------------------------------------------------|")
time.sleep(3)
input("Wcisnij klawisz ENTER:")
time.sleep(3)
print("Zamknij drzwi boczne autobusu!")
input("Wcisnij klawisz ENTER:")
time.sleep(3)
print("Autobus zjezdza na petle: ODPOCZYNEK 45 min. !")
time.sleep(3)
print()
#------------------------------------------------------------------------
# Koniec trasy , wyswietlenie raportu. [Drukuj]
#------------------------------------------------------------------------
time.sleep(3)
print("|------------------------------------------------------------|")
print("|-Koniec trasy autobusu:                                     |")
print("|------------------------------------------------------------|")
wybor = input ("Wybierasz ?")
print ()
time.sleep(3)
#------------------------------------------------------------------------
# Raport z trasy. [all]
#------------------------------------------------------------------------
print("|------------------------------------------------------------|")
print("| Koniec trasy autobusu: Drukwoanie raportu:                 |")
print("|------------------------------------------------------------|")
input ("[ENTER]")
time.sleep(1)
#--------------------------------------
# Liczenie sredniej predkosci autobusu
#--------------------------------------
print()
print("Srednia predkosc autobusu pomiedzy przystankami wyglada nastepujaco:")
SRPA1 =((V+V25+V50+V75+V100)/5)
time.sleep(3)
print(SRPA1,"|Km/h")
SRPA2 =((AV+AV25+AV50+AV75+AV100)/5,"|Km/h")
print(SRPA2)
SRPA3 =((BV+BV25+BV50+BV75+BV100)/5,"|Km/h")
print(SRPA3)
SRPA4 =((DV+DV25+DV50+DV75+DV100)/5,"|Km/h")
print(SRPA4)
SRPA5 =((EV+EV25+EV50+EV75+EV100)/5,"|Km/h")
print(SRPA5)
SRPA6 =((FV+FV25+FV50+FV75+FV100)/5,"|Km/h")
print(SRPA6)
SRPA7 =((GV+GV25+GV50+GV75+GV100)/5,"|Km/h")
print(SRPA7)
SRPA8 =[((SRPA1+SRPA2+SRPA3+SRPA4+SRPA5+SRPA6+SRPA7)/7)]
time.sleep(3)
print ("Srednia predkosc na tej lini autobusu wynosila:",(SRPA8),"|km/h")
print()
print(Liczba_Wsiadajacych,"osob")
print(BLiczba_Wsiadajacych,"osob")
print(CLiczba_Wsiadajacych,"osob")
print(DLiczba_Wsiadajacych,"osob")
print(ELiczba_Wsiadajacych,"osob")
print(FLiczba_Wsiadajacych,"osob")
print(GLiczba_Wsiadajacych,"osob")
SUM = [(Liczba_Wsiadajacych+BLiczba_Wsiadajacych+CLiczba_Wsiadajacych+DLiczba_Wsiadajacych+ELiczba_Wsiadajacych+FLiczba_Wsiadajacych+GLiczba_Wsiadajacych)]
print("Dzisiaj do autobusu lacznie wsiadlo:",SUM,"osob.")
SLP = [(Liczba_Wsiadajacych+BLiczba_Wsiadajacych+CLiczba_Wsiadajacych+DLiczba_Wsiadajacych+ELiczba_Wsiadajacych+FLiczba_Wsiadajacych+GLiczba_Wsiadajacych)/7]
time.sleep(3)
print("Srednio do autobusu co kazdy przystanek wsiadlo:",(SLP),"osob")
Trasa = (6)
Zbiornik_Autobusu = (500)
SR =[(Trasa*Zbiornik_Autobusu)/100]
print ("Srednie spalanie pojazdu na tym odcinku wynioslo:",(SR),"l/100km")
print()
time.sleep(3)
#------------------------------------------------------------------------
# Koniec programu
#------------------------------------------------------------------------
print("---------------------------------------------")
time.sleep(1)
print("End: %s" % time.ctime())
print("---------------------------------------------")
time.sleep(3)
input("[ENTER]")
print()
print("---------------------------------------------")
print("Zrodla oraz materialy pomocnicze:")
print("---------------------------------------------")
print("http://www.mpksieradz.pl/rozklad/4.html")
print("http://books.icse.us.edu.pl/runestone/static/thinkcspy/PythonModules/Therandommodule.html")
print("https://rk.edu.pl/pl/losowe-liczby-i-wartosci-z-sekwencji/")
print("---------------------------------------------")
input("Aby wyjsc z programu nacisnij klawisz [ENTER]")
sys.exit()
#------------------------------------------------------------------------
# Haslo logowania: qweas123
#-
# Program powstał do zaliczenia zadania z Podstaw Programowania
