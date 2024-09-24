tic_tac = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
pos = ['0', '1', '2']

print('To play the game type the position you want to mark X or O in your respective turn,\n '
      'to do so use two number the first number if to choose the line and the second number\n'
      'is to choose the row you want to mark. E.g: To mark the first spot use 00,\n'
      'to mark the middle spot use 11.')


def play(position, n_player):
    if len(position) != 2 or position[0] not in pos or position[1] not in pos:
        return play(input(f'Invalid input. Try again player {n_player}: '), n_player)
    if tic_tac[int(position[0])][int(position[1])] != ' ':
        play(input(f"This spot is marked already, try again player {player}: "), n_player)
    if player == 1:
        tic_tac[int(position[0])][int(position[1])] = 'X'
    else:
        tic_tac[int(position[0])][int(position[1])] = 'O'


def victory_check():
    for n in range(3):
        if tic_tac[n][0] == tic_tac[n][1] == tic_tac[n][2] != ' ':
            return True

        if tic_tac[0][n] == tic_tac[1][n] == tic_tac[2][n] != ' ':
            return True

    if tic_tac[0][0] == tic_tac[1][1] == tic_tac[2][2] != ' ':
        return True

    if tic_tac[0][2] == tic_tac[1][1] == tic_tac[2][0] != ' ':
        return True

    else:
        return False


def tic_tac_print():
    for i, row in enumerate(tic_tac):
        print(' | '.join(row) + ("\n -------" if i < len(tic_tac) - 1 else ""))


def is_draw():
    if all(slot != ' ' for row in tic_tac for slot in row):
        print('It is a draw')
        return True


game = True
player = 1
while game:
    tic_tac_print()

    play(input(f"Type where you want to mark X player {player}: "), player)

    if victory_check():
        print(f'Player {player} won!')
        break

    if is_draw():
        tic_tac_print()
        print("It's a draw.")
        break
    player = 2 if player == 1 else 1
