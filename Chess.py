# 2019-11-11 Chess with Python By CutyApple
# The white(bottom) is upper and the black(top) is lower
# King, Queen, Bishop, Knight, Rook, Pawn
# Each block has some piece or NULL

chessTable = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

def setTable():
    for i in range(0, 8):
        chessTable[0][0] = '♜'
        chessTable[0][1] = '♞'
        chessTable[0][2] = '♝'
        chessTable[0][3] = '♛'
        chessTable[0][4] = '♚'
        chessTable[0][5] = '♝'
        chessTable[0][6] = '♞'
        chessTable[0][7] = '♜'
        chessTable[1][i] = '♟'

        chessTable[7][0] = '♖'
        chessTable[7][1] = '♘'
        chessTable[7][2] = '♗'
        chessTable[7][3] = '♔'
        chessTable[7][4] = '♕'
        chessTable[7][5] = '♗'
        chessTable[7][6] = '♘'
        chessTable[7][7] = '♖'
        chessTable[6][i] = '♙'

def printTable():
    for i in range(0, 8):
        for j in range(0, 8):
            print(chessTable[i][j], end=' ')
        print('')

def chess():
    setTable()


###########################################################
# Below this line is the 『main function』.

chess()

printTable()

if('  ' == '  '):
    print(1)