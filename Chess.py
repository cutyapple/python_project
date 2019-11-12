# 2019-11-11 Chess with Python By CutyApple
# The white(bottom) is upper and the black(top) is lower
# King, Queen, Bishop, Knight, Rook, Pawn
# Each block has some piece or NULL
# turn True's means Black's turn and turn False's means White's turn
# remainB and remainW mean their remaining pieces

###########################################################
# variables' Space
turn = True
remainB = 0
remainW = 0

chessWidth =  ['ａ', 'ｂ', 'ｃ', 'ｄ', 'ｅ', 'ｆ', 'ｇ', 'ｈ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
chessHeight = ['１', '２', '３', '４', '５', '６', '７', '８']
whitePieces = ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜', '♟']
blackPieces = ['♖', '♘', '♗', '♔', '♕', '♗', '♘', '♖', '♙']
chessTable = [
    ['', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', ''],
]

def setTable():
    for i in range(0, 10):
        for j in range(0, 10):
            chessTable[i][j] = '　'

    for i in range(1, 9):
        chessTable[0][i] = chessWidth[i-1]
        chessTable[1][i] = blackPieces[i-1]
        chessTable[2][i] = blackPieces[8]
        chessTable[7][i] = whitePieces[8]
        chessTable[8][i] = whitePieces[i-1]
        chessTable[9][i] = chessWidth[i-1]
        chessTable[i][0] = chessHeight[i-1]
        chessTable[i][9] = chessHeight[i-1]

def printTable():
    for i in range(0, 10):
        for j in range(0, 10):
            print(chessTable[i][j], end=' ')

        print('')

def turnStart(turn):
    coor = input('select your piece : ')
    x, y = coor.strip().split(',')
    x = x.strip()
    y = y.strip()
    print(f'x : {x}')
    print(f'y : {y}')

def chess():
    setTable()

class piece():
    def move(self, x, y):
        print(x, y)
    def die(self):
        print('die')
    def sel(self):
        print(self)


###########################################################
# Below this line is the 『main function』.

chess()
printTable()

turnStart(True)
