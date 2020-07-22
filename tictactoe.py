theBoard = {'top-L': ' ', 'top-M' : ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M' : ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M' : ' ', 'low-R': ' '}

# print the board
def printBoard(board):
 print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
 print('-+-+-')
 print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
 print('-+-+-')
 print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

# function win to check if the player won the game
def win(board):
    boardValueList = list(board.values())
    constructBoard = []
    count = 0
    for i in range(3):
        tempList = []
        for j in range(3):
            tempList.append(boardValueList[count])
            count += 1
        constructBoard.append(tempList)
    columns = list(zip(*constructBoard)) 

    diagonalX_l = diagonalX_r = diagonalO_l = diagonalO_r = True
    for i in range(3):
        if all(x == 'X' for x in constructBoard[i]) or all(x == 'X' for x in columns[i]):
            print('Congrat X')
            return 1
        elif all(x == 'O' for x in constructBoard[i]) or all(x == 'O' for x in columns[i]):
            print('Congrat O')
            return 1
        if constructBoard[i][i] != 'X':
            diagonalX_l = False
        if constructBoard[i][2-i] != 'X':
            diagonalX_r = False
        if constructBoard[i][i] != 'O':
            diagonalO_l = False
        if constructBoard[i][2-i] != 'O':
            diagonalO_r = False  
        if i == 2:
            if diagonalX_l or diagonalX_r:
                print('Congrat X')
                return 1
            elif diagonalO_l or diagonalO_r:
                print('Congrat X')
                return 1


# give the player the chance to choose who will start
turn = ''
while True:
    turn = input('Who will start first X or O: ')
    if turn in ['X', 'O']:
        break
# make the moves
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    
    # check if the move is right, if not print for the user all possible positions
    while True:
        move = input()
        if move in theBoard.keys():
            if theBoard[move] == ' ':
                theBoard[move] = turn
                break
            else:
                print('Someone is there try different space: ')
        else:
            print('Choose from(', end='')
            for k, v in theBoard.items():
                if v == ' ': 
                    print(k, end=', ')
            print(')')
    
    #check for win
    if win(theBoard):
        break

    # change the turn of the person
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'


printBoard(theBoard)
