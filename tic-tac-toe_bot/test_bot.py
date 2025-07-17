from game import *
from minimax import *


def test_minimax_bot():
    """Test the minimax bot with various scenarios"""

    # Test 1: Bot should win when it can
    print("Test 1: Bot should win when it can")
    reset_board()
    # Set up a winning scenario for X (bot)
    gameboard[0][0] = PLAYER_X
    gameboard[0][1] = PLAYER_X
    # Bot should play at (0, 2) to win

    print("Board before bot move:")
    print_board()

    move = get_best_move(PLAYER_O)
    print(f"Bot chooses move: {move}")

    if move == (0, 2):
        print("✓ Test 1 PASSED: Bot chooses winning move")
    else:
        print("✗ Test 1 FAILED: Bot should choose (0, 2)")
        print(f"Expected: (0, 2), Got: {move}")

    print()

    # Test 2: Bot should block opponent's winning move
    print("Test 2: Bot should block opponent's winning move")
    reset_board()
    # Set up a scenario where O is about to win
    gameboard[1][0] = PLAYER_O
    gameboard[1][1] = PLAYER_O
    # Bot should play at (1, 2) to block

    print("Board before bot move:")
    print_board()

    move = get_best_move(PLAYER_O)
    print(f"Bot chooses move: {move}")

    if move == (1, 2):
        print("✓ Test 2 PASSED: Bot blocks opponent's winning move")
    else:
        print("✗ Test 2 FAILED: Bot should choose (1, 2)")
        print(f"Expected: (1, 2), Got: {move}")

    print()

    # Test 3: Bot should prefer center on empty board
    print("Test 3: Bot behavior on empty board")
    reset_board()

    print("Empty board:")
    print_board()

    move = get_best_move(PLAYER_O)
    print(f"Bot chooses move: {move}")

    # Center (1,1) is usually a good first move in tic-tac-toe
    if move == (1, 1):
        print("✓ Test 3 PASSED: Bot chooses center")
    else:
        print(f"Test 3 INFO: Bot chooses {move} (center is often optimal)")

    print()


if __name__ == "__main__":
    test_minimax_bot()
