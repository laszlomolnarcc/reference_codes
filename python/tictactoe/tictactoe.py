# tictactoe reference solution
#
# Laszlo Molnar, 2016, Codecool
import os

#global variables
table = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]
currentPlayer = "X"

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
        playTwoPlayerGame()
        return 1
    if "2" == userInput:
        print("Bye!")
    return 2

def playTwoPlayerGame():
    initGame()
    global currentPlayer
    currentPlayer = decideWhoStarts()
    doGameLoop()
    input("Press ENTER to go back to the Main Menu.")

def initGame():
    global table
    table = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]

def decideWhoStarts():
    clearScreen()
    whoStarts = ""
    while whoStarts != "X" and whoStarts != "O":
        whoStarts = input("'X'or 'O' should start the game (X/O)? ").upper()
    return whoStarts

def doGameLoop():
    global table
    drawTable()
    remainingSteps = len(table) * len(table[0])
    gameWon = False
    while gameWon == False and remainingSteps > 0:
        coords = getTableCoordsFromPlayer()
        while False == coordsAreValid(coords):
            print("The place you chosen is not empty!")
            coords = getTableCoordsFromPlayer()
        global currentPlayer
        table[coords[0]][coords[1]] = currentPlayer
        if True == gameFinished(coords):
            gameWon = True
        else:
            changeCurrentPlayer()
        drawTable()
        remainingSteps = remainingSteps - 1
    evaluateGameEnding(gameWon)

def drawTable():
    clearScreen()
    print("    A   B   C")
    print("  -------------")
    print("1 |", table[0][0], "|", table[1][0], "|", table[2][0], "|")
    print("  -------------")
    print("2 |", table[0][1], "|", table[1][1], "|", table[2][1], "|")
    print("  -------------")
    print("3 |", table[0][2], "|", table[1][2], "|", table[2][2], "|")
    print("  -------------")

def getTableCoordsFromPlayer():
    coords = (-1, -1)
    while coords[0] == -1 or coords[1] == -1:
        global currentPlayer
        nextMove = input("'" + currentPlayer + "', what is your next move(for ex. A2)? ")
        if len(nextMove) > 1:
            nextMove = nextMove.upper()
            coords = parsePlayerInput(nextMove)
    return coords

def parsePlayerInput(pInput):
    col = -1
    row = -1
    if pInput[0] == 'A':
        col = 0
    if pInput[0] == 'B':
        col = 1
    if pInput[0] == 'C':
        col = 2
    if pInput[1] == '1':
        row = 0
    if pInput[1] == '2':
        row = 1
    if pInput[1] == '3':
        row = 2
    return col, row

def coordsAreValid(coords):
    if table[coords[0]][coords[1]] == ".":
        return True
    return False

def changeCurrentPlayer():
    global currentPlayer
    if currentPlayer == "X": 
        currentPlayer = "O" 
    else:
        currentPlayer = "X"

def gameFinished(lastCoord):
    # check if the player won
    global currentPlayer

    # horizontal checking
    startPoint = checkSameItems(lastCoord, (-1, 0))
    endPoint = checkSameItems(lastCoord, (1, 0))
    if endPoint[0] - startPoint[0] >= 2:
       return True
    # vertical checking
    startPoint = checkSameItems(lastCoord, (0, -1))
    endPoint = checkSameItems(lastCoord, (0, 1))
    if endPoint[1] - startPoint[1] >= 2:
       return True
    # diagonal - left-to-right checking
    startPoint = checkSameItems(lastCoord, (-1, -1))
    endPoint = checkSameItems(lastCoord, (1, 1))
    if endPoint[0] - startPoint[0] >= 2:
       return True
    # diagonal - right-to-left checking
    startPoint = checkSameItems(lastCoord, (1, -1))
    endPoint = checkSameItems(lastCoord, (-1, 1))
    if abs(endPoint[0] - startPoint[0]) >= 2:
       return True

    return False

def checkSameItems(startCoord, incCoord):
    finalCoord = startCoord
    nextCoord = (finalCoord[0] + incCoord[0], finalCoord[1] + incCoord[1])

    while nextCoord[0] >= 0 and nextCoord[0] <= 2 and \
          nextCoord[1] >= 0 and nextCoord[1] <= 2 and \
          table[nextCoord[0]][nextCoord[1]] == currentPlayer:
        finalCoord = nextCoord
        nextCoord = (nextCoord[0] + incCoord[0], nextCoord[1] + incCoord[1])
    return finalCoord

def evaluateGameEnding(gameWon):
    if gameWon == True:
            print("'" + currentPlayer + "' won the game!")
    else:
        print("It's a draw!")

#main
menuDecision = 0
while menuDecision != 2:
    clearScreen()
    showWelcomeInfo()
    showMenu()
    menuDecision = processMenuDecision()
