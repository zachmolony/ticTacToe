#-------------------------------------------------------------------------------
# Name:        ticTacToe
#-------------------------------------------------------------------------------

board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", ]
xplayer = input("Player x enter your name: ")
oplayer = input("Player o enter your name: ")
x = True
print("The places on the board are denoted as follows: ")
print("0  1  2")
print("3  4  5")
print("6  7  8")

def main():
    global x
    try:
        if x == True:
            xmove = int(input(print(xplayer, "enter a number 0-8")))
            if board[xmove] == " ":
                board[xmove] = "x"
            else:
                print("That place is taken. try again")
                main()
        else:
            omove = int(input(print(oplayer, "enter a number 0-8")))
            if board[omove] == " ":
                board[omove] = "o"
            else:
                print("That place is taken. try again")
                main()
        x = not x
    except:
        print("invalid input. ")
        main()
    print_my_board()

def print_my_board():
    print(board[:3])
    print(board[3:6])
    print(board[6:9])
    isWin()

def isWin():
    #horizontal
    if (board[0] == "x" and board[1] == "x" and board[2] == "x") or (board[3] == "x" and board[4] == "x" and board[5] == "x") or (board[6] == "x" and board[7] == "x" and board[8] == "x"):
        print(xplayer, " wins")
    elif (board[0] == "o" and board[1] == "o" and board[2] == "o") or (board[3] == "o" and board[4] == "o" and board[5] == "o") or (board[6] == "o" and board[7] == "o" and board[8] == "o"):
        print(oplayer, " wins")
    #vertical
    elif (board[0] == "x" and board[3] == "x" and board[6] == "x") or (board[1] == "x" and board[4] == "x" and board[7] == "x") or (board[2] == "x" and board[5] == "x" and board[8] == "x"):
        print(xplayer, " wins")
    elif (board[0] == "o" and board[3] == "o" and board[6] == "o") or (board[1] == "o" and board[4] == "o" and board[7] == "o") or (board[2] == "o" and board[5] == "o" and board[8] == "o"):
        print(oplayer, " wins")
    #diagonal
    elif (board[0] == "x" and board[4] == "x" and board[8] == "x") or (board[2] == "x" and board[4] == "x" and board[6] == "x"):
        print(xplayer, " wins")
    elif (board[0] == "o" and board[4] == "o" and board[8] == "o") or (board[2] == "o" and board[4] == "o" and board[6] == "o"):
        print(oplayer, " wins")
    #check if the board is full
    elif " " not in board:
        print("the game is a tie ")
    else:
        main()
main()
