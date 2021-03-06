from os import system, name
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
        return int(len(board) / 2), int(len(board[0]) / 2)
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
    board_is_full = True
    for row in board:
        for col in row:
            if col == 0:
                board_is_full = False
    return board_is_full


def is_empty(board):
    """Returns True if board is empty."""
    board_is_empty = True
    for row in board:
        for col in row:
            if col != 0:
                board_is_empty = False
    return board_is_empty


def clear_screen():
    system('cls' if name == 'nt' else 'clear')


def print_board(board):
    """Prints a 3-by-3 board on the screen with borders."""
    clear_screen()
    row_letter = 65
    separator = "+"
    for col in range(len(board[0])):
        separator += "---+"
    print("\n    ", end="")
    for col in range(len(board[0])):
        print(f"{col + 1}", end="   ")
    print(f"\n  {separator}")
    for row in board:
        print(chr(row_letter) + " | " + str(row)
              .strip("[]")
              .replace(",", " |")
              .replace("0", " ")
              .replace("1", "X")
              .replace("2", "O") + " |")
        print(f"  {separator}")
        row_letter += 1


def print_result(winner, board):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    print_board(board)
    winner_sign = "X" if winner == 1 else "O"
    print("\nGAME OVER!\nIt's a tie!") if winner == 0 else print(
        f"\nGAME OVER!\nCongratulations!\nThe winner is Player {winner_sign}!")
    restart = input(">R<estart game: ").upper()
    if restart == "R":
        main_menu()
    else:
        print("Program is exiting...")
        quit()


def tictactoe_game(mode):
    if mode == 1:
        player = randint(1, 2)
        board = init_board()
        print_board(board)
        while not is_full(board):
            player = (1 if player == 2 else 2)
            row, col = get_move(board, player)
            mark(board, player, row, col)
            print_board(board)
            if has_won(board, player):
                winner = player
                print_result(winner, board)
                quit()
            if is_full(board):
                print_result(0, board)
                quit()
    else:
        player = randint(1, 2)
        board = init_board()
        print_board(board)
        while not is_full(board):
            player = (1 if player == 2 else 2)
            if player == 1:
                row, col = get_move(board, player)
                mark(board, player, row, col)
                print_board(board)
            else:
                row, col = get_ai_move(board)
                mark(board, player, row, col)
                print_board(board)
            if has_won(board, player):
                winner = player
                print_result(winner, board)
                quit()
            if is_full(board):
                print_result(0, board)
                quit()


def main_menu():
    clear_screen()
    print("\nWelcome to tic-tac-toe!\n\n1) HUMAN to HUMAN\n2) HUMAN to AI\n3) Quit")
    game_mode = input("\nChoose a mode: ")
    if game_mode in ['1', '2']:
        tictactoe_game(1) if game_mode == '1' else tictactoe_game(2)
    if game_mode == '3':
        print("Exiting...")
        quit()
    else:
        main_menu()


if __name__ == '__main__':
    main_menu()
