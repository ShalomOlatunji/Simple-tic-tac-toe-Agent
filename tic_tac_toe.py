"""A simple human-versus-computer Tic-Tac-Toe game."""

import random


def create_board():
    """Create and return an empty 3 x 3 game board."""
    return [" " for _ in range(9)]


def display_board(board):
    """Display the board in a readable format."""
    print(f"\n {board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}\n")


def check_winner(board, player):
    """Return True if player has three matching marks in a row."""
    winning_positions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    return any(all(board[position] == player for position in line)
               for line in winning_positions)


def check_tie(board):
    """Return True when all spaces are occupied and nobody has won."""
    return " " not in board and not check_winner(board, "X") and not check_winner(board, "O")


def find_winning_move(board, player):
    """Return a move that lets player win, if one exists."""
    for position in range(9):
        if board[position] == " ":
            board[position] = player
            wins = check_winner(board, player)
            board[position] = " "
            if wins:
                return position
    return None


def computer_move(board):
    """Choose a simple strategic move for the computer."""
    # Win if possible.
    move = find_winning_move(board, "O")
    if move is not None:
        return move

    # Block the user's winning move.
    move = find_winning_move(board, "X")
    if move is not None:
        return move

    # Prefer the centre, then a corner, then any free space.
    if board[4] == " ":
        return 4

    free_corners = [position for position in [0, 2, 6, 8]
                    if board[position] == " "]
    if free_corners:
        return random.choice(free_corners)

    free_spaces = [position for position in range(9) if board[position] == " "]
    return random.choice(free_spaces)


def get_user_move(board):
    """Ask the user for a valid position from 1 to 9."""
    while True:
        choice = input("Choose a position from 1 to 9: ").strip()

        if not choice.isdigit() or not 1 <= int(choice) <= 9:
            print("Please enter a number from 1 to 9.")
            continue

        position = int(choice) - 1
        if board[position] != " ":
            print("That position is already occupied.")
            continue

        return position


def play_game():
    """Run one complete game of Tic-Tac-Toe."""
    board = create_board()
    print("Welcome to Tic-Tac-Toe!")
    print("You are X. The computer is O.")
    print("Positions are numbered like this:")
    print(" 1 | 2 | 3\n---+---+---\n 4 | 5 | 6\n---+---+---\n 7 | 8 | 9")

    while True:
        display_board(board)
        user_position = get_user_move(board)
        board[user_position] = "X"

        if check_winner(board, "X"):
            display_board(board)
            print("You win!")
            break
        if check_tie(board):
            display_board(board)
            print("It's a tie!")
            break

        computer_position = computer_move(board)
        board[computer_position] = "O"
        print(f"The computer chose position {computer_position + 1}.")

        if check_winner(board, "O"):
            display_board(board)
            print("The computer wins!")
            break
        if check_tie(board):
            display_board(board)
            print("It's a tie!")
            break


if __name__ == "__main__":
    play_game()
