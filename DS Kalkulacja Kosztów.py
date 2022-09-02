import time
import sys
import random
from random import randint
print("---------------------------------------------")
print("Start: %s" % time.ctime())
print("---------------------------------------------")
print("Akademia Humanistyczno-Ekonoiczna w Łodzi")
print("---------------------------------------------")
print("Wydział : Informatyki , Zarządzania i Transportu")
print("Damian Skuras")
print("Kierunek:Informatyka III rok , V semestr")
print("Numer Indeksu:142873")
print("---------------------------------------------")
print("Przedmiot: Podstawy Programowania [LABOLATORIUM]-[ZADANIE 3]")
print("Nazwa: Kalkulacja Kosztów transportu samochodowego")
print("---------------------------------------------")
MiastoA = input("Podaj nazwę miasta poczatkowego:")
time.sleep(1)
print("---------------------------------------------")
MiastoB = input("Podaj nazwę miasta docelowego:")
time.sleep(1)
print("---------------------------------------------")
Odl1 = int(input("Podaj przybliżoną odległość pomiedzy maistami:"))
time.sleep(1)
print("---------------------------------------------")
print("Czy jest to przejazd w jedną stronę [T] czy z droga powrotna [N]? :")
Przejazd = input(":")
time.sleep(1)
T=1 #Tak
N=2 #NIE
if Przejazd ==1: #jeśli użytkownik wybierze odpowiedz T [TAK]
    print("---------------------------------------------")
    print("W jedna strone to sie oplaca.")
    print("End: %s" % time.ctime())
    print("---------------------------------------------")
    time.sleep(3)
    sys.exit()
    quit
lista =(random.randint(49,111)) #Predkosc przez trase w terenie zabudowanym 49-51 km/h lub na drodze szybkiego ruchu 95-111 km/h.
# ---------------------------------------------
# - Wzór na obliczenie czasu - .
#T=S/V
#S = Odl1
#T = none
#V = lista |-
# ---------------------------------------------
T=[Odl1/lista]
print("---------------------------------------------")
print("Trwa kalkulacja.Prosze czekac !")
print("---------------------------------------------")
for count in range (15):
    print(time.ctime())
    time.sleep(1)
time.sleep(3)
# ---------------------------------------------
print("---------------------------------------------")
print("Trasa: (",MiastoA,"-->",MiastoB,")")
print("Odległość:",Odl1,"KM","-> W jedna strone !!!")
print("Czas pokonania odleglosci pomiedzy miastami wynosi:",T,"min")
print("---------------------------------------------")
print("Poniedzialek:",Odl1*2,"KM")
print("Wtorek:",Odl1*2,"KM")
print("Sroda:",Odl1*2,"KM")
print("Czwartek:",Odl1*2,"KM")
print("Piatek:",Odl1*2,"KM")
print("---------------------------------------------")
print("Podsumowanie ilosci przebytych kilometrow od Pn do PT:",((Odl1*2)*5),"KM")
print("Podsumowanie ilosci przebytych kilometrow caly miesiac (30-31 dni):",(((Odl1*2)*5)*5),"KM")
print("---------------------------------------------")
time.sleep(1)
print("End: %s" % time.ctime())
print("---------------------------------------------")
time.sleep(3)
input("Aby wyjsc z programu nacisnij klawisz [ENTER]")
sys.exit()
# ---------------------------------------------
# ad.1 Trasa Sieradz -> Lodz.
# - Trasa 1: Sieradz->ZdunskaWola->Szadek->Lutomiersk->Konstantynów->Łódz.
# - Trasa 2: Sieradz->Lodz Droga S8 i S14. (~65 km lub 77 km).
# ---------------------------------------------
# ad.2 Trasa Sieradz -> Zgorzelec.
# - Trasa 1: Sieradz -> S8 -> A8 -> A4. (~320 km).
# ---------------------------------------------
----
