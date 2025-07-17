# Game dimensions
BOARD_WIDTH = 3
BOARD_HEIGHT = 3

# Game symbols
EMPTY = "_"
PLAYER_X = "X"
PLAYER_O = "O"

# Game board (global)
gameboard = [[EMPTY] * BOARD_WIDTH for _ in range(BOARD_HEIGHT)]


def print_board():
    """Print the game board"""
    print("  |   |   ")
    for row in range(BOARD_HEIGHT):
        for col in range(BOARD_WIDTH):
            if col == 2:
                print(f"{gameboard[row][col]}")
                break
            print(f"{gameboard[row][col]} | ", end='')

        if row != 2:
            print("  |   |   ")
            print("---------")
            print("  |   |   ")
    print("  |   |   ")


def print_board_with_positions():
    """Print board with position numbers for easy reference"""
    print("Positions:")
    print("  |   |   ")
    for row in range(BOARD_HEIGHT):
        for col in range(BOARD_WIDTH):
            pos = row * 3 + col + 1
            if col == 2:
                print(f"{pos}")
                break
            print(f"{pos} | ", end='')

        if row != 2:
            print("  |   |   ")
            print("---------")
            print("  |   |   ")
    print("  |   |   ")


def make_move(row, col, player):
    """Make a move on the board"""
    if gameboard[row][col] == EMPTY:
        gameboard[row][col] = player
        return True
    return False


def get_empty_cells(board):
    """Get list of empty cells"""
    empty_cells = []
    for row in range(BOARD_HEIGHT):
        for col in range(BOARD_WIDTH):
            if board[row][col] == EMPTY:
                empty_cells.append((row, col))
    return empty_cells


def reset_board():
    """Reset the game board"""
    for row in range(BOARD_HEIGHT):
        for col in range(BOARD_WIDTH):
            gameboard[row][col] = EMPTY


def is_game_over():
    """Check if the game is over"""
    return check_winner(gameboard) is not None or is_board_full(gameboard)


def is_board_full(board):
    """Check if the board is full"""
    for row in range(BOARD_HEIGHT):
        for col in range(BOARD_WIDTH):
            if board[row][col] == EMPTY:
                return False
    return True


def check_winner(board):
    """Check if there's a winner on the board"""
    # Check rows
    for row in range(BOARD_HEIGHT):
        if board[row][0] == board[row][1] == board[row][2] != EMPTY:
            return board[row][0]

    # Check columns
    for col in range(BOARD_WIDTH):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    return None
