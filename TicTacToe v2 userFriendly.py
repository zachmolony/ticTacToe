#-------------------------------------------------------------------------------
# Name:        ticTacToe
#-------------------------------------------------------------------------------
from time import sleep
#init board as list
board = [" ", " ", " ", " ", " ", " ", " ", " ", " ",]
print("=" * 40)
print("             TIC TAC TOE")
print("=" * 40)
print()
#name inputs
xplayer = input("Player x enter your name: ")
oplayer = input("Player o enter your name: ")
print()
#setting turn variable as boolean
x = True
print("The places on the board are denoted as follows: ")
boardE = list(range(1,10))
print(boardE[:3])
print(boardE[3:6])
print(boardE[6:])
print()

def main():
    global x
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
                main()
        else:
            omove = int(input('{} {}: '.format(oplayer, "enter a number 1-9"))) - 1
            if board[omove] == " ":
                board[omove] = "o"
            else:
                print("That place is taken. try again")
                main()
        #change current user
        x = not x
    #handles any invalid input
    except:
        print("invalid input. ")
        main()
    print_my_board()

def print_my_board():
    #printing each row of the board
    print(board[:3])
    print(board[3:6])
    print(board[6:])
    isWin()

def isWin():
    #horizontal win combinations
    if (board[0] == "x" and board[1] == "x" and board[2] == "x") or (board[3] == "x" and board[4] == "x" and board[5] == "x") or (board[6] == "x" and board[7] == "x" and board[8] == "x"):
        print(xplayer, " wins")
        sleep(5)
    elif (board[0] == "o" and board[1] == "o" and board[2] == "o") or (board[3] == "o" and board[4] == "o" and board[5] == "o") or (board[6] == "o" and board[7] == "o" and board[8] == "o"):
        print(oplayer, " wins")
        sleep(5)
    #vertical win combinations
    elif (board[0] == "x" and board[3] == "x" and board[6] == "x") or (board[1] == "x" and board[4] == "x" and board[7] == "x") or (board[2] == "x" and board[5] == "x" and board[8] == "x"):
        print(xplayer, " wins")
        sleep(5)
    elif (board[0] == "o" and board[3] == "o" and board[6] == "o") or (board[1] == "o" and board[4] == "o" and board[7] == "o") or (board[2] == "o" and board[5] == "o" and board[8] == "o"):
        print(oplayer, " wins")
        sleep(5)
    #diagonal win combinations
    elif (board[0] == "x" and board[4] == "x" and board[8] == "x") or (board[2] == "x" and board[4] == "x" and board[6] == "x"):
        print(xplayer, " wins")
        sleep(5)
    elif (board[0] == "o" and board[4] == "o" and board[8] == "o") or (board[2] == "o" and board[4] == "o" and board[6] == "o"):
        print(oplayer, " wins")
        sleep(5)
    #check if the board is full
    elif " " not in board:
        print("the game is a tie ")
        sleep(5)
    else:
        main()
main()
