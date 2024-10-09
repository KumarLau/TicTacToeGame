import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.reset_game()
        
        # Create buttons
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.root, text="", font=('Arial', 24), width=5, height=2,
                                   command=lambda r=row, c=col: self.make_move(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button
        
        # Reset button
        self.reset_button = tk.Button(self.root, text="Reset", font=('Arial', 14), command=self.reset_game)
        self.reset_button.grid(row=3, column=0, columnspan=3)
    
    def reset_game(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text="", state=tk.NORMAL)
    
    def make_move(self, row, col):
        if self.board[row][col] == '':
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner(self.current_player):
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.disable_buttons()
            elif self.check_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
    
    def check_winner(self, player):
        # Check rows, columns, and diagonals
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)) or \
               all(self.board[j][i] == player for j in range(3)):
                return True
        if (self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player) or \
           (self.board[0][2] == player and self.board[1][1] == player and self.board[2][0] == player):
            return True
        return False
    
    def check_draw(self):
        return all(self.board[row][col] != '' for row in range(3) for col in range(3))
    
    def disable_buttons(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
