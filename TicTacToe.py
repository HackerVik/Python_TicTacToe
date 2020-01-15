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

def get_ai_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    return row, col


def mark(board, player, row, col):
    """Marks the element at row & col on the board for player."""
    pass


def has_won(board, player):
    """Returns True if player has won the game."""
    return False


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