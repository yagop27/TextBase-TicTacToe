tic_tac = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
pos = ['0', '1', '2']

print('To play the game type the position you want to mark X or O in your respective turn,\n '
      'to do so use two number the first number if to choose the line and the second number\n'
      'is to choose the row you want to mark. E.g: To mark the first spot use 00,\n'
      'to mark the middle spot use 11.')


def player1(position):
    if len(position) != 2 or position[0] not in pos or position[1] not in pos:
        return player1(input('Invalid input. Try again player 1: '))
    if tic_tac[int(position[0])][int(position[1])] != ' ':
        player1(input("This spot is marked already, try again player 1: "))
    else:
        tic_tac[int(position[0])][int(position[1])] = 'X'


def player2(position):
    if len(position) != 2 or position[0] not in pos or position[1] not in pos:
        return player2(input('Invalid input. Try again player 2: '))
    if tic_tac[int(position[0])][int(position[1])] != ' ':
        player1(input("This spot is marked already, try again player 2: "))
    else:
        tic_tac[int(position[0])][int(position[1])] = 'O'


def victory_check():
    for n in range(3):
        if tic_tac[n].count(tic_tac[n][0]) == 3 and tic_tac[n][0] != ' ':
            return True

        column = [row[n] for row in tic_tac]
        if column.count(column[0]) == 3 and column[0] != ' ':
            return True

    diag1 = [tic_tac[n][n] for n in range(3)]
    if diag1.count(diag1[0]) == 3 and diag1[0] != ' ':
        return True

    diag2 = [tic_tac[n][2 - n] for n in range(3)]
    if diag2.count(diag2[0]) == 3 and diag2[0] != ' ':
        return True
    else:
        return False


def tic_tac_print():
    for i, row in enumerate(tic_tac):
        print(' | '.join(row) + ("\n -------" if i < len(tic_tac) - 1 else ""))
        

game = True
while game:
    tic_tac_print()

    player1(input("Type where you want to mark X player 1: "))
    tic_tac_print()

    if victory_check():
        print('Player 1 won!')
        break

    player2(input("Type where you want to mark O player 2: "))
    if victory_check():
        print('Player 2 won!')
        break



