import tkinter as tk
import random

class Puzzle8:
    def __init__(self, root):
        self.root = root
        self.root.title("8-Puzzle Game")
        self.board = []
        self.buttons = []
        self.create_board()
        self.shuffle_board()
        self.draw_board()

    def create_board(self):
        self.board = [[(i * 3 + j + 1) % 9 for j in range(3)] for i in range(3)]

    def draw_board(self):
        for i in range(3):
            for j in range(3):
                val = self.board[i][j]
                text = str(val) if val != 0 else ""
                if len(self.buttons) < 9:
                    btn = tk.Button(self.root, text=text, font=('Arial', 20), width=4, height=2,
                                    command=lambda i=i, j=j: self.move_tile(i, j))
                    btn.grid(row=i, column=j)
                    self.buttons.append(btn)
                else:
                    self.buttons[i * 3 + j].config(text=text)

    def move_tile(self, i, j):
        if self.board[i][j] == 0:
            return
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            ni, nj = i + dx, j + dy
            if 0 <= ni < 3 and 0 <= nj < 3 and self.board[ni][nj] == 0:
                self.board[ni][nj], self.board[i][j] = self.board[i][j], self.board[ni][nj]
                self.draw_board()
                if self.is_solved():
                    self.show_win_message()
                return

    def shuffle_board(self):
        for _ in range(100):
            i, j = random.randint(0,2), random.randint(0,2)
            self.move_tile(i, j)

    def is_solved(self):
        expected = [(i * 3 + j + 1) % 9 for i in range(3) for j in range(3)]
        current = [self.board[i][j] for i in range(3) for j in range(3)]
        return expected == current

    def show_win_message(self):
        win_label = tk.Label(self.root, text="You Solved It!", font=('Arial', 18), fg='green')
        win_label.grid(row=3, column=0, columnspan=3)

if __name__ == "__main__":
    root = tk.Tk()
    game = Puzzle8(root)
    root.mainloop()
