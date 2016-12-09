from random import randint
def player_one():
    return int(input("player one's turn (0-8)\n"))
def player_two():
    return int(input("player two's turn (0-8)\n"))
def random_choose():
    turn = randint(0,1)
    if turn == 0:#means that player one will go first, returns an even number for count
        return 2
    else:
        return 1#means that player 2 will go first, returns an odd number for count
def change_board(board, p1, p2):
    if count%2 == 0:#will change the placement to either X or O, depending on which players has played most recently
        board[p1] = "X"
    else:
        board[p2]= "O"

def print_board(board):
    for i in range(0,len(board)):
        if i==3 or i==6:
            print("\n")
        if i ==2 or i ==5 or i==8:
            print(board[i], end = "")
            
        else:
            print(board[i] + "|", end = "")
    print('\n------')
def space_check(board, p1, p2):
    if board[p1] == " " or board[p2] == " ":
        return True
    else:
        print("Sorry, this spot has already been filled, Try again")
        return False
def board_full(board):
    full = True
    for i in range(0,len(board)):
        if board[i] == " ":
            full = False
            break
    return full
def win(board):
    if board[0] == board[1] == board[2]=="X" or board[3] == board[4] == board[5]=="X" or board[6] == board[7] == board[8]=="X" or \
    board[0] == board[3] == board[6]=="X" or board[1] == board[4] == board[7]=="X" or board[2] == board[5] == board[8]=="X" or \
    board[0] == board[4] == board[8]=="X" or board[2] == board[4] == board[6]=="X":
        x = input("Player 1 wins, restart game? (Y/N)")
        if x =="Y" or x == "y":
            return True
        else:
            return False
    elif board[0] == board[1] == board[2]=="O" or board[3] == board[4] == board[5]=="O" or board[6] == board[7] == board[8]=="O" or \
    board[0] == board[3] == board[6]=="O" or board[1] == board[4] == board[7]=="O" or board[2] == board[5] == board[8]=="O" or \
    board[0] == board[4] == board[8]=="O" or board[2] == board[4] == board[6]=="O":
        y = input("Player 2 wins, restart game? (Y/N)")
        if y =="Y" or y == "y":
            return True
        else:
            return False
    elif board_full(board) == True:
        z = input("Nobody won, the board is full, Restart? (Y/N)")
        if z== "Y" or z == "y":
            return True
        else:
            return False
def reset_board():
    global board 
    global loop
    global p1
    global p2
    global count
    board = [" "]*9
    p1 = -1
    p2 = -1
    count = 0
    loop = False
reset_board()

while True:
    
    while loop == False:
        
        if count == 0:
            count = random_choose()
        if count%2 == 0:
            p1 = player_one() 
        elif count %2 != 0:
            p2 = player_two()
        loop = space_check(board, p1, p2)
        
    change_board(board, p1, p2)       
    print_board(board)
    cont = win(board)
    
    if cont == False:
        break
    elif cont == True:
        reset_board()
    else:
        count+=1
        loop = False

    