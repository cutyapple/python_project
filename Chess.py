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
chessHeight = ['８', '７', '６', '５', '４', '３', '２', '１', '8', '7', '6', '5', '4', '3', '2', '1']
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
            print(chessTable[i][j], end='')

        print('')

def turnStart(turn):
    coor = input('select your piece : ')
    x, y = coor.strip().split(',')
    x = x.strip()
    y = y.strip()
    print(f'x : {x}')
    print(f'y : {y}')
    check(chessWidth, chessHeight, x, y)

def check(piecesXList, piecesYList, x, y):
    xIndex = None
    yIndex = None
    for i in piecesXList:
        if x == i :
            xIndex = piecesXList.index(i) - 7

    for i in piecesYList:
        if y == i:
            yIndex = piecesYList.index(i) - 7

    print(f'xIndex : {xIndex}, yIndex : {yIndex}')

    if xIndex != None and yIndex != None:
        if chessTable[xIndex][yIndex] == '　' :
            print('There is no one')
        else :
            print(chessTable[xIndex][yIndex])

def chess():
    setTable()

class piece:
    direction = []          #moveable direction
    distance = 0            #moveable distance
    aDis = 0                #auxiliary distance

    def move(self, x, y):   #piece's moving
        print(x, y)

    def die(self):          #piece's dying
        print('die')

    def sel(self):          #piece's selecting
        print(self)

class King(piece):
    def __init__(self):
        self.distance = 1
        self.direction = [1, 2, 3, 4, 6, 7, 8, 9]
        self.moved = False  #castling

class Queen(piece):
    def __init__(self):
        self.distance = 7
        self.direction = [1, 2, 3, 4, 6, 7, 8, 9]

class Bishop(piece):
    def __init__(self):
        self.distance = 7
        self.direction = [1, 3, 7, 9]

class Knight(piece):
    def __init__(self):
        self.distance = 2
        self.direction = [1, 3, 7, 9]
        self.aDis = 1

class Rook(piece):
    def __init__(self):
        self.distance = 7
        self.direction = [2, 4, 6, 8]
        self.moved = False  #castling

class Pawn(piece):
    def __init__(self):
        self.distance = 1
        self.direction = [8]
        self.aDis = 1

###########################################################
# Below this line is the 『main function』.

chess()
printTable()

turnStart(True)
