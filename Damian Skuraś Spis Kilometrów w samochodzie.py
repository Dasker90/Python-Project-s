print("-------------------")
print("Damian Skuraś")
print("Informatyka III rok")
print("Nr.Alb: 142873")
print("Wydział Informatyki")
print("Uczelnia: A.H.E Łódz")
print("-------------------")
#---
print("Program do spisu kilometrów w twoim samochodzie V0.1")
spisy = []
choice = None
import time
time = time.strftime("%Y %B %d - %H:%M:%S",time.gmtime())
while choice != "0":
	print(
	"""
	0 - zakoncz
	1 - pokaz spis kilometrów.
	2 - dodaj spisane kilometry.
	"""
	)
	choice = input("wybierasz: ")
# zakoncz program
	if choice == "0":
		print("Dziękuje i do widzenia. ")
		print(time)
		break
# wypisz tabele najlepszych wynikow i sortuje odrazu
	elif choice == "1":	
		print("Spis kilometrów \n")
		print("-------------------")
		print(KMprzed,KMpo,'Zatankowane Paliwo:',Wlane,'L','Kilometry:',kilometry,'KM')
		print("-------------------")
		#for Entry in spisy:
			#KMpo, Wlane = Entry
			#print(Entry)

	elif choice == "2":
		KMprzed = int(input("Podaj ilość kilometrow ostatniego tankowania: "))
		KMpo = int(input("Podaj ilość kilometrow po tankowaniu: "))
		Wlane = float(input("Podaj ilość zatankowanego paliwa:"))
		kilometry = (KMpo-KMprzed)
		print("Ilość przejechanych kilometrów to:",kilometry,'km')
		paliwo =((Wlane/kilometry)*100)
		print("Średnie spalanie wynosi:",paliwo,'/100km')
		print("-------------------------------------------------------------")
		Entry =(KMpo,Wlane)
                #spisy.extend(Entry)
                #spisy.sort(reverse=True)
               
#nieznana opcja

else:
    print("niestety,", choice, "nie jest prawidlowym wyborem.")


input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
