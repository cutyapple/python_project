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
    moved = True            #piece's moving check
    team = ''               #piece's team

    def die(self):          #piece's dying
        if self.team:
            print(f'White team\'s King dead!')
            print(f'Black team win!')
            game_end = True
        self.is_dying = True


class King(Piece):
    def __init__(self, x, y, name, symbol, team):
        self.distance = 1
        self.direction = [[-1, 1], [0, 1], [1, 1], [-1, 0], [1, 0], [-1, -1], [0, -1], [1, -1]]
        self.location = [x, y]          #[a, 1]
        self.moved = False  #castling
        self.name = name
        self.symbol = symbol
        self.team = team


class Queen(Piece):
    def __init__(self, x, y, name, symbol, team):
        self.distance = 7
        self.direction = [[-1, 1], [0, 1], [1, 1], [-1, 0], [1, 0], [-1, -1], [0, -1], [1, -1]]
        self.location = [x, y]
        self.name = name
        self.symbol = symbol
        self.team = team


class Bishop(Piece):
    def __init__(self, x, y, name, symbol, team):
        self.distance = 7
        self.direction = [[-1, 1], [0, 0], [1, 1], [0, 0], [0, 0], [-1, -1], [0, 0], [1, -1]]
        self.location = [x, y]
        self.name = name
        self.symbol = symbol
        self.team = team


class Knight(Piece):
    def __init__(self, x, y, name, symbol, team):
        self.distance = 2
        self.direction = [[0, 0], [0, 1], [0, 0], [-1, 0], [1, 0], [0, 0], [0, -1], [0, 0]]
        self.location = [x, y]
        self.au_dis = 1
        self.name = name
        self.symbol = symbol
        self.team = team


class Rook(Piece):
    def __init__(self, x, y, name, symbol, team):
        self.distance = 7
        self.direction = [[0, 0], [0, 1], [0, 0], [-1, 0], [1, 0], [0, 0], [0, -1], [0, 0]]
        self.location = [x, y]
        self.moved = False  #castling
        self.name = name
        self.symbol = symbol
        self.team = team


class Pawn(Piece):
    def __init__(self, x, y, name, symbol, team, directions):
        self.distance = 1
        self.direction = directions
        self.location = [x, y]
        self.au_dis = 1       #special moving
        self.moved = False    #first moving
        self.name = name
        self.symbol = symbol
        self.team = team


game_end = False

wPawnDir = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, -1], [0, 0]]
bPawnDir = [[0, 0], [0, 1], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

bRookA = Rook('a', 8, 'bRookA', '♖', True)
bKnightA = Knight('b', 8, 'bKnightA', '♘', True)
bBishopA = Bishop('c', 8, 'bBishopA', '♗', True)
bQueen = Queen('e', 8, 'bQueen', '♔', True)
bKing = King('d', 8, 'bKing', '♕', True)
bBishopB = Bishop('f', 8, 'bBishopB', '♗', True)
bKnightB = Knight('g', 8, 'bKnightB', '♘', True)
bRookB = Rook('h', 8, 'bRookB', '♖', True)

bPawnA = Pawn('a', 7, 'bPawnA', '♙', True, bPawnDir)
bPawnB = Pawn('b', 7, 'bPawnB', '♙', True, bPawnDir)
bPawnC = Pawn('c', 7, 'bPawnC', '♙', True, bPawnDir)
bPawnD = Pawn('d', 7, 'bPawnD', '♙', True, bPawnDir)
bPawnE = Pawn('e', 7, 'bPawnE', '♙', True, bPawnDir)
bPawnF = Pawn('f', 7, 'bPawnF', '♙', True, bPawnDir)
bPawnG = Pawn('g', 7, 'bPawnG', '♙', True, bPawnDir)
bPawnH = Pawn('h', 7, 'bPawnH', '♙', True, bPawnDir)

wPawnA = Pawn('a', 2, 'wPawnA', '♟', False, wPawnDir)
wPawnB = Pawn('b', 2, 'wPawnB', '♟', False, wPawnDir)
wPawnC = Pawn('c', 2, 'wPawnC', '♟', False, wPawnDir)
wPawnD = Pawn('d', 2, 'wPawnD', '♟', False, wPawnDir)
wPawnE = Pawn('e', 2, 'wPawnE', '♟', False, wPawnDir)
wPawnF = Pawn('f', 2, 'wPawnF', '♟', False, wPawnDir)
wPawnG = Pawn('g', 2, 'wPawnG', '♟', False, wPawnDir)
wPawnH = Pawn('h', 2, 'wPawnH', '♟', False, wPawnDir)

wRookA = Rook('a', 1, 'wRookA', '♜', False)
wKnightA = Knight('b', 1, 'wKnightA', '♞', False)
wBishopA = Bishop('c', 1, 'wBishopA', '♝', False)
wQueen = Queen('e', 1, 'wQueen', '♚', False)
wKing = King('d', 1, 'wKing', '♛', False)
wBishopB = Bishop('f', 1, 'wBishopB', '♝', False)
wKnightB = Knight('g', 1, 'wKnightB', '♞', False)
wRookB = Rook('h', 1, 'wRookB', '♜', False)

piece_list = [
    bRookA, bKnightA, bBishopA, bKing, bQueen, bBishopB, bKnightB, bRookB,
    bPawnA, bPawnB, bPawnC, bPawnD, bPawnE, bPawnF, bPawnG, bPawnH,
    wPawnA, wPawnB, wPawnC, wPawnD, wPawnE, wPawnF, wPawnG, wPawnH,
    wRookA, wKnightA, wBishopA, wKing, wQueen, wBishopB, wKnightB, wRookB,
]

###########################################################
# variables' Space
turn = False
remain_b = 0
remain_w = 0

chess_width = ['ａ', 'ｂ', 'ｃ', 'ｄ', 'ｅ', 'ｆ', 'ｇ', 'ｈ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
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

    return [table_x, table_y]


def re_table():   # table modify
    for piece in piece_list:
        x, y = piece.location

        if not x == y == -1:
            code_list = table_to_code(x, y)
            code_x, code_y = code_list
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

def table_color_set(table_color):
    x_index, y_index, indexes = [], [], []
    if table_color != []:
        for i in table_color:
            x_index.append(i[0])
            y_index.append(i[1])

    for i in range(0, int(len(x_index))):
        indexes.append([x_index[i], y_index[i]])

    return indexes

def print_table(table_color):  # print the current table
    cls()

    indexes = table_color_set(table_color)

    if turn:
        print('Black team\'s turn')
    else:
        print('White team\'s turn')

    for i in range(0, 10):
        for j in range(0, 10):
                check = True
                check2 = True
                for index in indexes:
                    if index == [j, i]:
                        for piece in piece_list:
                            table_x, table_y = code_to_table(j, i)
                            table_y = int(table_y)
                            if piece.location == [table_x, table_y]:
                                if piece.team != turn:
                                    print(f'\x1b[0;0;45m{chess_table[i][j]}\x1b[0m', end='')
                                    check2 = False
                                    check = False
                        if check2:
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


def inputing(word):
    x = ''
    y = ''

    while(True):
        try:
            coor = input(word)
            x, y = coor.strip().split(',')
            x = x.strip()
            y = y.strip()

            y = int(y)
            if not (y in chess_height):
                y = '+'
            if not (x in chess_width):
                y = '+'
            y = int(y)
            break

        except ValueError:
            print(f'ERROR : wrong input.')

    return [x, y]


def selecting(x, y):
    y = int(y)
    x_index, y_index = table_to_code(x, y)
    y_index = int(y_index)

    color_add(find_piece(x, y))

    indexes = table_color_set(table_color)

    if chess_table[y_index][x_index] == '　':
        print_table(table_color)
        print('There is no one')
        turn_start()
    elif indexes == []:
        print_table(table_color)
        print('It can\'t move there')
        turn_start()
    elif find_piece(x, y).team != turn:
        color_del()
        print_table(table_color)
        print('It isn\'t your team')
        turn_start()
    else:
        for piece in piece_list:
            if piece.location == [x, y]:
                print(f'Your choice : [{x}, {y}] : {chess_table[y_index][x_index]}')
                indexes = table_color_set(table_color)
                while(True):
                    input_x, input_y = inputing('select the coordinates : ')
                    x, y = table_to_code(input_x, input_y)
                    y = int(y)

                    if [x, y] in indexes:
                        break
                    print('ERROR : wrong choice.')

                print(f'Your choice : [{input_x}, {input_y}]')

                move(input_x, input_y, piece)


def find_piece(input_x, input_y):
    for piece in piece_list:
        if piece.location == [input_x, input_y]:
            return piece


# table_color에 들어있는 쓰레기 값 제거
def color_del():
    for i in range(0, len(table_color)):
        table_color.pop()


def color_add(piece):
    color_del()

    if piece == None:
        return

    x, y = piece.location
    x, y = table_to_code(x, y)
    x = int(x)
    y = int(y)
    for direction in piece.direction:
        dir_x, dir_y = direction
        if not dir_x == dir_y == 0:
            for i in range(0, piece.distance+1):
                check = True
                move_x = x + i * dir_x
                move_y = y + i * dir_y

                #Is it a Knight?
                if 'Knight' in piece.name:
                    ys = [-1, 1, -2, 2, -2, 2, -1, 1]
                    xs = [-2, -2, -1, -1, 1, 1, 2, 2]
                    for i in range(0, 8):
                        check = True
                        move_x = xs[i] + x
                        move_y = ys[i] + y

                        if move_x < 1 or move_y < 1 or move_x > 8 or move_y > 8:
                            check = False

                        if check:
                            move_c_x, move_c_y = code_to_table(move_x, move_y)
                            move_piece = find_piece(move_c_x, move_c_y)
                            if move_piece != None:
                                if move_piece.team == turn:
                                    check = False


                            if check:
                                if not [move_x, move_y] in table_color:
                                    table_color.append([move_x, move_y])
                                    check = False
                    check = False

                if check:

                    # Is there the wall?
                    if move_x < 1 or move_y < 1 or move_x > 8 or move_y > 8:
                        break

                    # Is it a Pawn?
                    if 'Pawn' in piece.name:
                        sub = 0
                        if not piece.team:
                            sub = -1
                        else:
                            sub = 1

                        for i in range(-1, 2):
                            table_x, table_y = code_to_table(move_x + i, move_y + sub)
                            pawn_someone = find_piece(table_x, table_y)

                            if i == 0 and pawn_someone != None:
                                continue

                            if i != 0 and pawn_someone == None:
                                continue
                            elif i != 0 and pawn_someone != None:
                                if pawn_someone.team == piece.team:
                                    continue

                            table_color.append([move_x + i, move_y + sub])

                        if not piece.moved:
                            table_color.append([move_x, (move_y + sub * 2)])
                            piece.moved = True
                            break

                    # Is there something?
                    if i != 0 and chess_table[move_y][move_x] != '　':
                        for something in piece_list:
                            t_move_x, t_move_y = code_to_table(move_x, move_y)
                            t_move_y = int(t_move_y)
                            if something.location == [t_move_x, t_move_y]:
                                if something.team != piece.team:
                                    table_color.append([move_x, move_y])
                        break

                    if i != 0:
                        table_color.append([move_x, move_y])
    print_table(table_color)

    
def move(x, y, piece):
    pre_x, pre_y = piece.location
    pre_x, pre_y = table_to_code(pre_x, pre_y)

    pre_x = int(pre_x)
    pre_y = int(pre_y)
    chess_table[pre_y][pre_x] = '　'

    attaked_piece = find_piece(x, y)

    if attaked_piece != None:
        attaked_piece.location = [-1, -1]
        attaked_piece.is_dying = True
        if 'King' in attaked_piece.name:
            attaked_piece.die()

    x, y = table_to_code(x, y)

    for color_coor in table_color:
        coor_x, coor_y = color_coor
        if x == coor_x and y == coor_y:
            x, y = code_to_table(x, y)
            piece.location = [x, y]

    for i in range(0, len(table_color)):
        table_color.pop()

    re_table()
    print_table(table_color)


def chess():
    set_table()
    print_table(table_color)
    global turn

    while (not game_end):
        turn_start()
        turn = not turn


def turn_start():
    color_del()
    input_x, input_y = inputing('select your piece : ')
    selecting(input_x, input_y)

###########################################################
# Below this line is the 『main function』.


chess()

# 너무 하드코딩 아닌가?