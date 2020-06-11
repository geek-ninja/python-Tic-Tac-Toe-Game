import random
 
#Creating the game board
board = [' ' for _ in range(9)]
 
def insertMove(le,pos):
    board[pos] = le
    
def isFreeSpace(pos):
    return board[pos] == ' '

def isWinner(bo,le):
    #All possible combinations of winning pattern
    return ((bo[0] == le and  bo[1] == le and bo[2] == le) or 
            (bo[3] == le and  bo[4] == le and bo[5] == le) or 
            (bo[6] == le and  bo[7] == le and bo[8] == le) or
            (bo[0] == le and  bo[4] == le and bo[8] == le) or
            (bo[2] == le and  bo[4] == le and bo[6] == le) or
            (bo[0] == le and  bo[3] == le and bo[6] == le) or
            (bo[1] == le and  bo[4] == le and bo[7] == le) or
            (bo[2] == le and  bo[5] == le and bo[8] == le))
    
def printBoard(board):
    print('     |     |   ')
    print('  '+board[0]+'  |  '+board[1]+'  |  '+board[2]+'   ')
    print('     |     |   ')
    print('-----------------')
    print('     |     |   ')
    print('  '+board[3]+'  |  '+board[4]+'  |  '+board[5]+'   ')
    print('     |     |   ')
    print('-----------------')
    print('     |     |   ')
    print('  '+board[6]+'  |  '+board[7]+'  |  '+board[8]+'   ')
    print('     |     |   ')

def isBoardFull(board):
    if board.count(' ') > 0:
        return False
    else:
        return True

def playerMove():
    myTurn = True
    while myTurn:
        move = int(input('Please select a position for X (1-9): \n'))
        move = move-1 #To match the index in board array
        try:
            if move >=0 and move <9:
                if isFreeSpace(move):
                    myTurn = False
                    insertMove('X',move)
                else:
                    print('Position is occupied !\n')
            else:
                print("Enter position in the range !\n")
        except:
            print("Enter a valid position ! \n")

def aiMove():
    possibleMoves = [m for m,le in enumerate(board) if le == ' ']
    aimove = -1
    for le in ['O','X']:
        for i in possibleMoves:
            copyBoard = board.copy()
            copyBoard[i] = le
            if isWinner(copyBoard,le):
                aimove = i
                return aimove
    #Try to occupy a random corner
    openCorner = []
    for i in possibleMoves:
        corners = [0,2,6,8]
        if i in corners:
            openCorner.append(i)
    if len(openCorner) > 0:
        aimove = random.choice(openCorner)
        return aimove
    
    #Try to occupy center of the board

    if 4 in possibleMoves:
        aimove = 5
        return aimove
    
    #Try to occupy an edge of the board
    openEdge = []
    for i in possibleMoves:
        edge = [1,3,5,7]
        if i in edge:
            openEdge.append(i)
    if len(openEdge) > 0:
        aimove = random.choice(openEdge)
        return aimove
    return aimove
    
def main():
    print("----X--O-----Welcome to Tic Tac Toe Game.----O---X----")
    print("The board positions are 1-9 starting from left\n")
    printBoard(board)
    while not(isBoardFull(board)):
        if not(isWinner(board,'O')):
            playerMove()
            printBoard(board)
        else:
            print('Ai wins the match !\n')
            break
        
        if not(isWinner(board,'X')):
            move = aiMove()
            if move == -1:
                print('Game Tie !')
                break
            else:
                insertMove('O',move)
                print('Ai place O in position ',move+1,'\n')
                printBoard(board)
        else:
            print('X win ,congo !\n')
            break
        
    if isBoardFull(board):
        print('Game is Tie ,no space is left\n')
        
while True:
    ans = input('Do you want to play?(Y/N)\n')
    if ans.lower() == 'y':
        board = [' ' for _ in range(9)]
        main()
    else:
        break
    
