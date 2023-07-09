class incorrectInput(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self) :
        return self.msg

def printBoard(board, move):
    print(f"\nAfter {move+1} move :\n")
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            print(board[i][j]+' | ', end=' ')
        print()
    print()


def horizontal_win(board):
    win = False
    for i in range(0, len(board)):
        l = board[i]
        if (l == ['X', 'X', 'X'] or l == ['O', 'O', 'O']):
            win = True
    return win


def vertical_win(board):
    win = False
    for i in range(0, len(board)):
        l = []
        for j in range(0, len(board)):
            l.append(board[j][i])
        if (l == ['X', 'X', 'X'] or l == ['O', 'O', 'O']):
            win = True
            break
    return win


def diagonal_win(board):
    d1 = [board[0][0], board[1][1], board[2][2]]
    d2 = [board[0][2], board[1][1], board[2][0]]
    win = False
    if (d1 == ['X', 'X', 'X'] or d1 == ['O', 'O', 'O']):
        win = True
    if (d2 == ['X', 'X', 'X'] or d2 == ['O', 'O', 'O']):
        win = True
    return win


def validateInput(list):
    if len(list) < 2:
        try:
            raise incorrectInput("Invalid Input: Please both row and column number.")
        except incorrectInput as e:
            print(e)
    else:
        try:
            r, c = int(list[0]), int(list[1])
        except:
            print("\nPlease Enter Valid Row and Column number (1-3)\n")
        else:
            if (r >= 1 and r <= 3) and (c >= 1 and c <= 3):
                return r, c
            else:
                try:
                    raise incorrectInput("Please Enter valid Row and Column number (1-3)")
                except incorrectInput as e:
                    print(e)
                    exit


print("'X'--WELCOME TO TIC-TAC-TOE GAME--'O'".center(45))
print()

firstplayername = input("Enter 'X' player name: ")
secondplayername = input("Enter 'O' player name: ")
print()
board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
movescount = 0
firstplayersym, secondplayersym = 'X', 'O'
visited = set()
first, second = True, False
while (movescount < 9):
    if (first == True):
        try:
            r, c = validateInput(
                input("Enter which row and column u need to insert('X'): ").split())

        except:
            break
            

        else:
            if (r, c) not in visited:
                visited.add((r, c))
                board[r-1][c-1] = 'X'
                printBoard(board, movescount)
                movescount += 1
                first, second = False, True
                if (horizontal_win(board) == True or vertical_win(board) == True or diagonal_win(board) == True):
                    print(f"\n{firstplayername} is the winner\n")
                    break
            else:
                try:
                    raise incorrectInput("\nAlready The cell is occuiped! Please a Enter a valid row and column number\n")
                except incorrectInput as e:
                   print(e)
                   break


    else:
        try:
            r, c = list(
                map(int, input("Enter which row and column u need to insert('O'): ").split()))
        except:
            break
        else:
            if (r, c) not in visited:
                visited.add((r, c))
                board[r-1][c-1] = 'O'
                printBoard(board, movescount)
                movescount += 1
                first, second = True, False
                if (horizontal_win(board) == True or vertical_win(board) == True or diagonal_win(board) == True):
                    print(f"\n{secondplayername} is the winner\n")
                    break
            else:
                try:
                    raise incorrectInput("\nAlready The cell is occuiped! Please a Enter a valid row and column number\n")
                except incorrectInput as e:
                   print(e)
                   break



else:
    print("\nThe match is tie")
