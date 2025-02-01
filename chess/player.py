import tkinter as tk
from tkinter import *
import piece


class Player:
    def __init__(self):
        self.root = tk.Tk()

    def display(self):
        self.root.title("Player Selection")
        tk.Label(self.root, text="Player 1: ").grid(row=0, column=0)
        tk.Label(self.root, text="Player 2: ").grid(row=1, column=0)
        player1_entry = tk.Entry(self.root)
        player1_entry.grid(row=0, column=1)
        player2_entry = tk.Entry(self.root)
        player2_entry.grid(row=1, column=1)
        tk.Button(self.root, text="Start game", anchor="ne", command=piece.g).grid(
            row=2, column=1
        )
        self.root.mainloop()
