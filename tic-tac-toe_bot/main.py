from game import *


def get_human_move():
    """Get move from human player"""
    while True:
        try:
            position = int(input("Enter your move (1-9): "))
            if 1 <= position <= 9:
                row = (position - 1) // 3
                col = (position - 1) % 3
                if gameboard[row][col] == EMPTY:
                    return row, col
                else:
                    print("That position is already taken!")
            else:
                print("Please enter a number between 1 and 9!")
        except ValueError:
            print("Please enter a valid number!")


def play_game():
    """Play the game between two players"""
    move_count = 0

    print_board_with_positions()
    print()

    while not is_game_over():
        print_board()
        print()

        if move_count % 2 == 0:
            print("Player X turn:")
            row, col = get_human_move()
            make_move(row, col, PLAYER_X)
        else:
            print("Player 0 turn:")
            row, col = get_human_move()
            make_move(row, col, PLAYER_O)

        move_count += 1

    if move_count % 2 == 0:
        print("Player O won")
        print_board()
    else:
        print("Player X won")
        print_board()


def play_with_ai():
    print("TODO...")


def game_loop():
    """Main game loop"""
    while True:
        print("1: Play with AI (default)")
        print("2: Play with friend")
        game_mode = input("Select (1-2): ")

        if game_mode == "1":
            reset_board()
            play_with_ai()
        elif game_mode == "2":
            reset_board()
            play_game()
        elif game_mode == "":
            reset_board()
            play_with_ai()
        else:
            print(f"Invalid value: {game_mode}")
            continue

        play_again = input("\nWould you like to play again? (y/N): ")
        play_again.lower().strip()

        if play_again != 'y' and play_again != 'yes':
            print("Thanks for playing!")
            break


def main():
    game_loop()


if __name__ == "__main__":
    main()
