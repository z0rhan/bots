from game import *

# TODO: optimize this with alpha-beta pruning
def minimax(board, depth, isMaximizing):
    """Minimax algorithm that returns certain score for every move"""
    winner = check_winner(board)
    if winner == PLAYER_X:
        return 10 - depth
    elif winner == PLAYER_O:
        return depth - 10
    elif not get_empty_cells(board):  # Game is a draw
        return 0

    moves = get_empty_cells(board)
    if isMaximizing:
        best_score = float('-inf')
        for row, col in moves:
            board[row][col] = PLAYER_X
            score = minimax(board, depth + 1, False)
            board[row][col] = EMPTY
            best_score = max(best_score, score)
    else:
        best_score = float('inf')
        for row, col in moves:
            board[row][col] = PLAYER_O
            score = minimax(board, depth + 1, True)
            board[row][col] = EMPTY
            best_score = min(best_score, score)

    return best_score


def get_best_move(player):
    """Call minimax for every possible moves"""
    best_score = float('-inf') if player == PLAYER_X else float('inf')
    best_move = None
    possible_moves = get_empty_cells(gameboard)

    for row, col in possible_moves:
        gameboard[row][col] = player

        if player == PLAYER_X:
            score = minimax(gameboard, 0, False)
            if score > best_score:
                best_score = score
                best_move = (row, col)
        else:  # player == PLAYER_O
            score = minimax(gameboard, 0, True)
            if score < best_score:
                best_score = score
                best_move = (row, col)

        gameboard[row][col] = EMPTY

    return best_move


def ai_make_move():
    """Helper that makes the move for AI"""
    row, col = get_best_move(PLAYER_O)
    make_move(row, col, PLAYER_O)
    print(f"Human plays at ({row}, {col})")
