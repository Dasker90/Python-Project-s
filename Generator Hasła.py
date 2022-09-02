#sposób łatwy---
import random
print("-----------------------------")
print("Damian Skuras")
print("Informatyka III Rok | Technologie Programowania")
print("Nr:142873")
s = 'ABCDEFGHIJKLMNOPRSTUWXYZabcdefghijklmnoprstuwxyz1234567890!@#'
dlugosc_hasla = 8
haslo = ["".join(random.sample(s,dlugosc_hasla))]
print("-----------------------------")
print("Twoje haslo to:",haslo)
#sposób trudniejszy
import random
import string
def generuj_haslo(size = 8, chars=string.ascii_letters + string.digits +string.punctuation):
    return ''.join(random.choice(chars) for _ in range(size))
print("-----------------------------")
input("Mam wygenerować inne hasla? |ENTER|")
print("-----------------------------")
haslo = int(input("Jaka ma być długosc hasla?:"))
print("-----------------------------")
print("Twoje hasło to:","|",generuj_haslo(haslo),"|")
print("-----------------------------")
input("Czy chces więcej przykladowych 10 haseł ?: [ENTER]")
print("-----------------------------")
print("Hasło 2:",generuj_haslo(haslo))
print("Hasło 3:",generuj_haslo(haslo))
print("Hasło 4:",generuj_haslo(haslo))
print("Hasło 5:",generuj_haslo(haslo))
print("Hasło 6:",generuj_haslo(haslo))
print("Hasło 7:",generuj_haslo(haslo))
print("Hasło 8:",generuj_haslo(haslo))
print("Hasło 9:",generuj_haslo(haslo))
print("Hasło 10:",generuj_haslo(haslo))
print("-----------------------------")
input("Aby wyjsc z programu nacisnij klawisz |ENTER|")
choice = 0
if choice == 0:
    quit()
