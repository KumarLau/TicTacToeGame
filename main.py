class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.game_over = False

    def print_board(self):
        print("Current board:")
        for row in range(3):
            print("|".join(self.board[row]))
            if row < 2:
                print("-----")

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            if self.check_winner(self.current_player):
                self.print_board()
                print(f"Player {self.current_player} wins!")
                self.game_over = True
            elif self.check_draw():
                self.print_board()
                print("It's a draw!")
                self.game_over = True
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
        else:
            print("This position is already taken. Try again.")

    def check_winner(self, player):
        # Check rows, columns, and diagonals for a win
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)) or \
               all(self.board[j][i] == player for j in range(3)):
                return True
        if (self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player) or \
           (self.board[0][2] == player and self.board[1][1] == player and self.board[2][0] == player):
            return True
        return False

    def check_draw(self):
        return all(self.board[row][col] != ' ' for row in range(3) for col in range(3))

    def play(self):
        print("Welcome to Tic Tac Toe!")
        self.print_board()
        while not self.game_over:
            try:
                row = int(input(f"Player {self.current_player}, enter the row (0, 1, 2): "))
                col = int(input(f"Player {self.current_player}, enter the column (0, 1, 2): "))
                if row in [0, 1, 2] and col in [0, 1, 2]:
                    self.make_move(row, col)
                    if not self.game_over:
                        self.print_board()
                else:
                    print("Invalid input. Please enter numbers between 0 and 2.")
            except ValueError:
                print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    game = TicTacToe()
    game.play()

