from random import randint


def init_board():
    """Returns an empty 3-by-3 board (with zeros)."""
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    return board

def get_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row_list = [chr(row + 65) for row in range(len(board))]
    col_list = [str(row + 1) for row in range(len(board))]
    player_sign = "X" if player == 1 else "O"
    print("")
    player_input = input(f"Enter your move Player {player_sign}: ").upper()
    if player_input == "QUIT":
        print("Exiting...")
        quit()
    while player_input[0] not in row_list \
            or player_input[1] not in col_list:
        player_input = input(f"First enter row as {row_list} then enter col as {col_list}: ").upper()
    row, col = ord(player_input[0]) - 65, int(player_input[1]) - 1
    while board[row][col] != 0:
        player_input = input(f"That's already taken!Enter your move Player {player_sign}: ").upper()
        while player_input[0] not in row_list \
                or player_input[1] not in col_list:
            player_input = input(f"First enter row as {row_list} then enter col as {col_list}: ").upper()
        row, col = ord(player_input[0]) - 65, int(player_input[1]) - 1
    return row, col

def get_ai_move(board):
    """Returns the coordinates of a valid move for player on board."""
    if is_empty(board):
        return int(len(board)/2), int(len(board[0])/2)
    else:
        row, col = randint(0, len(board[0]) - 1), randint(0, len(board) - 1)
        while board[row][col] != 0:
            row, col = randint(0, len(board[0]) - 1), randint(0, len(board) - 1)
        return row, col

def mark(board, player, row, col):
    """Marks the element at row & col on the board for player."""
    board[row][col] = player

def has_won(board, player):
    """Returns True if player has won the game."""
    return True if (board[0][0] == player and board[0][1] == player and board[0][2] == player or
                    board[1][0] == player and board[1][1] == player and board[1][2] == player or
                    board[2][0] == player and board[2][1] == player and board[2][2] == player or
                    board[0][0] == player and board[1][0] == player and board[2][0] == player or
                    board[0][1] == player and board[1][1] == player and board[2][1] == player or
                    board[0][2] == player and board[1][2] == player and board[2][2] == player or
                    board[0][0] == player and board[1][1] == player and board[2][2] == player or
                    board[0][2] == player and board[1][1] == player and board[2][0] == player) else False

def is_full(board):
    """Returns True if board is full."""
    return False


def print_board(board):
    """Prints a 3-by-3 board on the screen with borders."""
    pass


def print_result(winner):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    pass


def tictactoe_game(mode='HUMAN-HUMAN'):
    board = init_board()

    # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
    print_board(board)
    row, col = get_move(board, 1)
    mark(board, 1, row, col)

    winner = 0
    print_result(winner)


def main_menu():
    tictactoe_game('HUMAN-HUMAN')


if __name__ == '__main__':
    main_menu()