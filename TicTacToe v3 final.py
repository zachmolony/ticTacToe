#-------------------------------------------------------------------------------
# Name:        ticTacToe
#-------------------------------------------------------------------------------
from time import sleep
from random import randint
#init board as list
print("=" * 40)
print("             TIC TAC TOE")
print("=" * 40)
print()
print("The places on the board are denoted as follows: ")
boardExample = list(range(1,10))
print(boardExample[:3])
print(boardExample[3:6])
print(boardExample[6:])
print()
#setting turn variable as boolean
x = True
won = False

#this function runs the selection of what mode the user chooses
def start():
    global players, oplayer, xplayer, mode, board
    try:
        board = [" ", " ", " ", " ", " ", " ", " ", " ", " ",]
        players = int(input("Enter a 1 for a one player game and a 2 for a two player game, or a 3 to exit: "))
        if players == 1:
            xplayer = input("Player x enter your name: ")
            mode = "e"
            cpuEasy()
        elif players == 2:
            xplayer = input("Player x enter your name: ")
            oplayer = input("Player o enter your name: ")
            twoPlayer()
    except:
        print("Invalid input. ")
        sleep(2)
        start()

#takes inputs from users and places them on the board
def twoPlayer():
    global xplayer, oplayer, x
    try:
        #check for users turn
        if x == True:
            #choose placement
            xmove = int(input('{} {}: '.format(xplayer, "enter a number 1-9"))) - 1
            #check if the space is free
            if board[xmove] == " ":
                board[xmove] = "x"
            else:
                print("That place is taken. try again")
                twoPlayer()
        else:
            omove = int(input('{} {}: '.format(oplayer, "enter a number 1-9"))) - 1
            if board[omove] == " ":
                board[omove] = "o"
            else:
                print("That place is taken. try again")
                twoPlayer()
        #change current user
        x = not x
    #handles any invalid input
    except:
        print("invalid input")
        twoPlayer()
    print_my_board()

#this function is identical to the 2player function but instead generates a random integer intead of taking an input
def cpuEasy():
    global x, won, xplayer, oplayer
    try:
        #check for users turn
        if x == True:
            #choose placement
            xmove = int(input('{} {}: '.format(xplayer, "enter a number 1-9"))) - 1
            #check if the space is free
            if board[xmove] == " ":
                board[xmove] = "x"
            else:
                print("That place is taken. try again")
                twoPlayer()
        else:
            omove = randint(0,9)
            if board[omove] == " ":
                board[omove] = "o"
                omove += 1
                print("CPU chooses space", omove)
            else:
                cpuEasy()
        #change current user
        x = not x
    #handles any invalid input
    except:
        print("invalid input. ")
        cpuEasy()
    print_my_board()

#prints the lines of the board
def print_my_board():
    #printing each row of the board
    print(board[:3])
    print(board[3:6])
    print(board[6:])
    isWin()

#fuction checks all possible win scenarios
def isWin():
    global players, mode, won
    #horizontal win combinations
    if (board[0] == "x" and board[1] == "x" and board[2] == "x") or (board[3] == "x" and board[4] == "x" and board[5] == "x") or (board[6] == "x" and board[7] == "x" and board[8] == "x"):
        print(xplayer, " wins")
        won = True
    elif (board[0] == "o" and board[1] == "o" and board[2] == "o") or (board[3] == "o" and board[4] == "o" and board[5] == "o") or (board[6] == "o" and board[7] == "o" and board[8] == "o"):
        print(oplayer, " wins")
        won = True
    #vertical win combinations
    elif (board[0] == "x" and board[3] == "x" and board[6] == "x") or (board[1] == "x" and board[4] == "x" and board[7] == "x") or (board[2] == "x" and board[5] == "x" and board[8] == "x"):
        print(xplayer, " wins")
        won = True
    elif (board[0] == "o" and board[3] == "o" and board[6] == "o") or (board[1] == "o" and board[4] == "o" and board[7] == "o") or (board[2] == "o" and board[5] == "o" and board[8] == "o"):
        print(oplayer, " wins")
        won = True
    #diagonal win combinations
    elif (board[0] == "x" and board[4] == "x" and board[8] == "x") or (board[2] == "x" and board[4] == "x" and board[6] == "x"):
        print(xplayer, " wins")
        won = True
    elif (board[0] == "o" and board[4] == "o" and board[8] == "o") or (board[2] == "o" and board[4] == "o" and board[6] == "o"):
        print(oplayer, " wins")
        won = True
    #check if the board is full
    elif " " not in board:
        print("the game is a tie ")
        won = True
    #check if the game is over
    if won == True:
        print("Game over.")
        start()
    #continue game if nobody has won
    elif players == 1:
        if mode == "e":
            cpuEasy()
        elif mode == "h":
            cpuHard()
    elif players == 2:
        twoPlayer()

start()
