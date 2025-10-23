def print_board(board):
    """Display the current state of the board."""
    print("\nCurrent Board:")
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("--+---+--")
    print()


def check_winner(board):
    """Check all rows, columns, and diagonals for a winner."""
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None


def tic_tac_toe():
    """Main function to run the Tic-Tac-Toe game."""
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    moves = 0
    winner = None

    while True:
        print_board(board)

        # Get user input safely
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
        except ValueError:
            print("❌ Invalid input! Please enter numbers 0, 1, or 2.")
            continue

        # Check valid range
        if not (0 <= row < 3 and 0 <= col < 3):
            print("⚠️ Coordinates out of range! Please enter values between 0 and 2.")
            continue

        # Check if spot is already taken
        if board[row][col] != " ":
            print("❗ That spot is already taken! Try again.")
            continue

        # Make the move
        board[row][col] = player
        moves += 1

        # Check for a winner
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"🎉 Player {winner} wins! Congratulations!")
            break

        # Check for draw
        if moves == 9:
            print_board(board)
            print("🤝 It's a draw! No more moves left.")
            break

        # Switch player
        player = "O" if player == "X" else "X"


# Run the game
if __name__ == "__main__":
    tic_tac_toe()
