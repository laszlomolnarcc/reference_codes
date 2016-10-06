# tictactoe reference solution
#
# Laszlo Molnar, 2016, Codecool
import os

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def showWelcomeInfo():
    print("--- TicTacToe ---\n")
    print("Welcome! The goal of the game is to make three X's or O's in a line.")
    print("The line can be in a column/row or it can be diagonal.\n")

def showMenu():
    print("1. PLAY GAME (2 player)")
    print("2. QUIT\n")

def processMenuDecision():
    userInput = ""
    while (userInput != "1" and userInput != "2"):
        userInput = input("Choose from the numbers (write 1 or 2 and press ENTER): ")
    if "1" == userInput:
        startTwoPlayerGame()
    if "2" == userInput:
        print("Bye!")

def startTwoPlayerGame():
    print("Start the game!!")

clearScreen()
showWelcomeInfo()
showMenu()
processMenuDecision()
