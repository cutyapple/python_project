# 2019-11-11 Chess with Python By CutyApple
# The white(bottom) is upper and the black(top) is lower
# King, Queen, Bishop, Knight, Rook, Pawn
# Each block has some piece or NULL
# turn True's means Black's turn and turn False's means White's turn
# remainB and remainW mean their remaining pieces
# Table is filled with black and white color
# Castling, En passant, promotion, check, checkmate, touch-move, stalemate
##########################################################

class Piece:
    symbol = ''             #piece's symbol
    name = ''               #piece's unique name
    location = []           #current location (table)
    code_lo = []             #current loocation (code - array)
    direction = [[]]          #moveable direction
    distance = 0            #moveable distance
    au_dis = 0                #auxiliary distance
    is_dying = False         #piece's checking

    def move(self, x, y):   #piece's moving
        print(x, y)

    def die(self):          #piece's dying
        print('die')
        self.is_dying = True

    def select(self):       #piece's selecting
        print(self)

    def checking(self):     #available check checking
        print(self)


class King(Piece):
    def __init__(self, x, y, name, symbol):
        self.distance = 1
        self.direction = [[-1, 1], [0, 1], [1, 1], [-1, 0], [1, 0], [-1, -1], [0, -1], [1, -1]]
        self.location = [x, y]          #[a, 1]
        self.moved = False  #castling
        self.name = name
        self.symbol = symbol


class Queen(Piece):
    def __init__(self, x, y, name, symbol):
        self.distance = 7
        self.direction = [[-1, 1], [0, 1], [1, 1], [-1, 0], [1, 0], [-1, -1], [0, -1], [1, -1]]
        self.location = [x, y]
        self.name = name
        self.symbol = symbol


class Bishop(Piece):
    def __init__(self, x, y, name, symbol):
        self.distance = 7
        self.direction = [[-1, 1], [0, 0], [1, 1], [0, 0], [0, 0], [-1, -1], [0, 0], [1, -1]]
        self.location = [x, y]
        self.name = name
        self.symbol = symbol


class Knight(Piece):                            #
    def __init__(self, x, y, name, symbol):     #
        self.distance = 2                       #
        self.direction = [1, 3, 7, 9]           #knight should be modify
        self.location = [x, y]                  #
        self.au_dis = 1       #special moving   #
        self.name = name                        #
        self.symbol = symbol                    #


class Rook(Piece):
    def __init__(self, x, y, name, symbol):
        self.distance = 7
        self.direction = [[0, 0], [0, 1], [0, 0], [-1, 0], [1, 0], [0, 0], [0, -1], [0, 0]]
        self.location = [x, y]
        self.moved = False  #castling
        self.name = name
        self.symbol = symbol


class Pawn(Piece):
    def __init__(self, x, y, name, symbol):
        self.distance = 1
        self.direction = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, -1], [0, 0]]
        self.location = [x, y]
        self.au_dis = 1       #special moving
        self.moved = False  #first moving
        self.name = name
        self.symbol = symbol

bRookA = Rook('a', 8, 'bRookA', '♖')
bKnightA = Knight('b', 8, 'bKnightA', '♘')
bBishopA = Bishop('c', 8, 'bBishopA', '♗')
bQueen = Queen('e', 8, 'bQueen', '♔')
bKing = King('d', 8, 'bKing', '♕')
bBishopB = Bishop('f', 8, 'bBishopB', '♗')
bKnightB = Knight('g', 8, 'bKnightB', '♘')
bRookB = Rook('h', 8, 'bRookB', '♖')

bPawnA = Pawn('a', 7, 'bPawnA', '♙')
bPawnB = Pawn('b', 7, 'bPawnB', '♙')
bPawnC = Pawn('c', 7, 'bPawnC', '♙')
bPawnD = Pawn('d', 7, 'bPawnD', '♙')
bPawnE = Pawn('e', 7, 'bPawnE', '♙')
bPawnF = Pawn('f', 7, 'bPawnF', '♙')
bPawnG = Pawn('g', 7, 'bPawnG', '♙')
bPawnH = Pawn('h', 7, 'bPawnH', '♙')

wPawnA = Pawn('a', 2, 'wPawnA', '♟')
wPawnB = Pawn('b', 2, 'wPawnB', '♟')
wPawnC = Pawn('c', 2, 'wPawnC', '♟')
wPawnD = Pawn('d', 2, 'wPawnD', '♟')
wPawnE = Pawn('e', 2, 'wPawnE', '♟')
wPawnF = Pawn('f', 2, 'wPawnF', '♟')
wPawnG = Pawn('g', 2, 'wPawnG', '♟')
wPawnH = Pawn('h', 2, 'wPawnH', '♟')

wRookA = Rook('a', 1, 'wRookA', '♜')
wKnightA = Knight('b', 1, 'wKnightA', '♞')
wBishopA = Bishop('c', 1, 'wBishopA', '♝')
wQueen = Queen('e', 1, 'wQueen', '♚')
wKing = King('d', 1, 'wKing', '♛')
wBishopB = Bishop('f', 1, 'wBishopB', '♝')
wKnightB = Knight('g', 1, 'wKnightB', '♞')
wRookB = Rook('h', 1, 'wRookB', '♜')

piece_list = [
    bRookA, bKnightA, bBishopA, bKing, bQueen, bBishopB, bKnightB, bRookB,
    bPawnA, bPawnB, bPawnC, bPawnD, bPawnE, bPawnF, bPawnG, bPawnH,
    wPawnA, wPawnB, wPawnC, wPawnD, wPawnE, wPawnF, wPawnG, wPawnH,
    wRookA, wKnightA, wBishopA, wKing, wQueen, wBishopB, wKnightB, wRookB,
]

###########################################################
# variables' Space
turn = True
remain_b = 0
remain_w = 0

chess_width =  ['ａ', 'ｂ', 'ｃ', 'ｄ', 'ｅ', 'ｆ', 'ｇ', 'ｈ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
chess_height = ['８', '７', '６', '５', '４', '３', '２', '１', 8, 7, 6, 5, 4, 3, 2, 1]
chess_table = [
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

table_color = [[]]
table_color.pop(0)

def cls():
    print('\n'*50)


def table_to_code(table_x, table_y):    # table's coor change to array's coor
    array_x = None
    array_y = None

    for i in chess_width:
        if i == table_x:
            array_x = chess_width.index(i) - 7

    for i in chess_height:
        if i == table_y:
            array_y = chess_height[i - 9]

    return [array_x, array_y]


def code_to_table(array_x, array_y):  # array's coor change to table's coor
    table_x = chess_width[array_x + 7]
    table_y = chess_height[array_y + 7]

    print(f'[{table_x}, {table_y}]')

    return [table_x, table_y]


def re_table():   # table modify
    for piece in piece_list:
        x, y = piece.location
        code_list = table_to_code(x, y)
        code_x, code_y = code_list
        print(f'{piece.symbol} : {piece.name} :  x = {code_x}, y = {code_y}')
        chess_table[code_y][code_x] = piece.symbol


def set_table():  # before the start, setting the table
    for i in range(0, 10):
        for j in range(0, 10):
            chess_table[i][j] = '　'

    for i in range(1, 9):
        chess_table[0][i] = chess_width[i - 1]
        chess_table[9][i] = chess_width[i - 1]
        chess_table[i][0] = chess_height[i - 1]
        chess_table[i][9] = chess_height[i - 1]

    for piece in piece_list:
        x, y = piece.location
        code_list = table_to_code(x, y)
        code_x, code_y = code_list
        chess_table[code_y][code_x] = piece.symbol


def print_table():  # print the current table
    global table_color
    cls()
    x_index, y_index, indexes = [], [], []
    if table_color != []:
        for i in table_color:
            x_index.append(i[0])
            y_index.append(i[1])

    for i in range(0, int(len(x_index))):
        indexes.append([x_index[i], y_index[i]])

    for i in range(0, 10):
        for j in range(0, 10):
                check = True
                for index in indexes:
                    if index == [j, i]:
                        print(f'\x1b[0;0;46m{chess_table[i][j]}\x1b[0m', end='')
                        check = False

                if check:
                    if i == 0 or j == 0 or i == 9 or j == 9:
                        print(f'{chess_table[i][j]}', end='')
                    elif (j+i) % 2 == 0:
                        print(f'\x1b[0;0;40m{chess_table[i][j]}\x1b[0m', end='')
                    else:
                        print(f'\x1b[0;0;0m{chess_table[i][j]}\x1b[0m', end='')

        print('')

    table_color = [[]]
    table_color.pop()


def inputing(word):
    coor = ''
    x = ''
    y = ''
    error = False

    while(True):
        try:
            coor = input(word)
            x, y = coor.strip().split(',')
            x = x.strip()
            y = y.strip()

            y = int(y)
            if not y in chess_height:
                y = '+'
            if not x in chess_width:
                y = '+'
            y = int(y)
            error = True
            if error == True:
                break
        except ValueError:
            print(f'ERROR : wrong input.')
            error = False

    return [x, y]


def list_check(x, y):
    x_index = ''
    y_index = ''
    for i in chess_width:
        if x == i:
            x_index = chess_width.index(i) - 7

    for i in chess_height:
        if y == i:
            y_index = chess_height.index(i) - 7

    return [x_index, y_index]


def moving(pieces_x_list, pieces_y_list, x, y):
    x_index = None
    y_index = None
    y = int(y)

    x_index, y_index = list_check(x, y)
    y_index = int(y_index)

    find(x, y)

    print_table()

    if x_index != None and y_index != None:
        if chess_table[y_index][x_index] == '　':
            print('There is no one')
            turn_start()
        else:
            for piece in piece_list:
                if piece.location == [x, y]:
                    print(f'Your choice : [{x}, {y}] : {chess_table[y_index][x_index]}')
                    input_x, input_y = inputing('select the coordinates : ')
                    input_y = int(input_y)

                    list_x, list_y= list_check(input_x, input_y)

                    print(f'Your choice : [{input_x}, {input_y}]')

                    find(x, y)


def find(input_x, input_y):
    for piece in piece_list:
        if piece.location == [input_x, input_y]:
            direct(piece)

def direct(piece):
    x, y = piece.location
    x, y = table_to_code(x, y)
    x = int(x)
    y = int(y)
    for direction in piece.direction:
        dir_x, dir_y = direction
        if not dir_x == dir_y == 0:
            for i in range (0, piece.distance+1):
                move_x = x + i * dir_x
                move_y = y + i * dir_y

                if  move_x < 1 or move_y < 1 or move_x > 8 or move_y > 8 :
                    break

                if i != 0 and chess_table[move_y][move_x] != '　':
                    break
                
                if i != 0 :
                    table_color.append([move_x, move_y])

def chess():
    set_table()


def turn_start():
    input_x, input_y = inputing('select your piece : ')
    moving(chess_width, chess_height, input_x, input_y)

###########################################################
# Below this line is the 『main function』.

chess()
print_table()

# 너무 하드코딩 아닌가?


turn_start()
print_table()