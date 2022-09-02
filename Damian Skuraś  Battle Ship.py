import time             #biblioteka czasu
import datetime
import sys
import random
from random import randint
#-
print("---------------------------------------------")
print("Mateusz Markun | Informatyka III Rok")
print("Zaawansowane Technologie Programowania | Projekt ")
print("---------------------------------------------")
print("v: 0.1 z 04.07.2022 r.")
print("---------------------------------------------")
print("Start: %s" % time.ctime())
print("---------------------------------------------")
board = []

for x in range(6):
    board.append(["O"] * 6)

def print_board(board):
    for row in board:
        print((" ").join(row))

print("Let's play Battleship!")
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)
def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

for turn in range(9):
    print ("Turn"), turn
    guess_row = int(input("Guess Row:"))
    guess_col = int(
        input("Guess Col:"))

    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sunk my battleship!")
        break
    else:
        if (guess_row < 0 or guess_row > 5) or (guess_col < 0 or guess_col > 5):
            print("Oops, that's not even in the ocean.")
        elif(board[guess_row][guess_col] == "X"):
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"
    if turn == 8:
        print("Game Over")
    turn =+ 1
    print_board(board)
print("---------------------------------------------")
time.sleep(1)
print("End: %s" % time.ctime())
print("---------------------------------------------")
time.sleep(3)
input("Aby wyjsc z programu nacisnij klawisz [ENTER]")
sys.exit()
