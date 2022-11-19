import sys
import time

print()
time.sleep(2)
def mainMenu():
    while True :
        print()
        print('''### SHOPPING LIST ###
        
        Select a number for the action that you would like to do:
        
        1.View shopping list
        2.Add item to shopping list
        3.Remove item from shopping list
        4.Chceck if item is on shopping list
        5.How many items on shopping list
        6.Clear shopping list
        7.Exit
        ''')
        selection = input("Make your selection:" + " ?")
        if selection == "1":
            displayList()
        elif seceltion == "2":
            addItem()
        elif seceltion == "3":
            removeItem()
        elif seceltion == "4":
            checkItem()
        elif seceltion == "5":
            listLenght()
        elif seceltion == "6":
            pass
        elif seceltion == "7":
            print("Ari vederci ROMA :)")
            sys.exit()
        else:
            print("You did not make a valid seleciotn.")
#-------------------------------------------------
# Shopping List:
shopping_list = ["apples","bananas","carrots","potatoes","orange","lemon","mango","melon","pear","plum","strawberry","watermelon","bluberry"]
#-------------------------------------------------
def displayList():
    print()
    print("---SHOPPING LIST ---")
    for i in shopping_list:
        print("* " + i)
#-------------------------------------------------
# Definicje do listy od 1 do 7: ------------------
#-------------------------------------------------
def addItem():
    item = input ("Enter the item you wish to add to the shopping list: ")
    shopping_list.append(item)
    time.sleep(2)
    print(item + "has been added to the shopping list.")
#-------------------------------------------------
def removeItem():
    item = input ("Enter the item you wish to remove from the shopping list: ")
    shopping_list.remove(item)
    time.sleep(2)
    print(item + "has been removed from the shopping list.")
#-------------------------------------------------
def checkItem():
    item = input("What item would you like to check on the shopping list: ")
    if item in shopping_list:
        print("Yes ," + item + " that item is on the shopping list. ")
    else:
        print("No , " + item + " that item is not on the shopping list. ")
#-------------------------------------------------
def listLenght():
    print("There are", len(shopping_list), "items on the shopping list.")
#-------------------------------------------------
def clearList():
    shopping_list.clear()
    print("The shopping list is now empty. ")
#-------------------------------------------------



# Run the function mainMenu - which will run our app
mainMenu()
print("---------------------------")














