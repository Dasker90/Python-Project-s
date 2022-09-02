import random
print ("----------------------------")
print ("Damian Skuraś / A.H.E / 2021")
print ("Liczby losowe do jackpota")
print ("----------------------------")

gramy = "tak"

podane = []
wylosowane = []

while gramy == "tak":
    for i in range (7):
        podane.append(int(input("Podaj liczbe :"+str(i+1)+":")))
        wylosowane.append(random.randint(1,49))
    trafione = 0
    for z in podane:
        for j in wylosowane:
            if z ==j :
                trafione = trafione + 1
    print ("----------------------------")
    print("Twoje traafione liczby to :"+str(trafione))
    print ("----------------------------")
    print("Wylosowane liczby w Jackpocie to:")
    print ("----------------------------")
    for i in wylosowane:
        print(i)
    podane.clear()
    wylosowane.clear()
    print ("----------------------------")
    gramy = input("Czy losujesz jeszcze raz ? (TAK/NIE)")
    print ("----------------------------")
while gramy == "nie":
    print ("Dziękuje i dowidzenia")
    sys.pause
#--
