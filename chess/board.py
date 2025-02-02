import tkinter as tk
import piece


class Board:
    def __init__(self):
        self.button_1 = None

    def butto(self, button_2):
        self.move = Board.move
        if self.button_1 is None:
            self.button_1 = button_2
        else:
            ii = self.button_1.grid_info()
            row, column = ii["row"], ii["column"]
            i = button_2.grid_info()
            r, c = i["row"], i["column"]
            if piece.cek_move(row, column, r, c):
                self.move(self.button_1, button_2)
                self.button_1 = None
            else:
                self.button_1 = None
    def move(button_1, button_2):
        text1, bg1, fg1 = button_1["text"], button_1["bg"], button_1["fg"]
        button_1["text"], button_1["bg"], button_1["fg"] = (
            button_2["text"],
            button_2["bg"],
            button_2["fg"],
        )
        button_2["text"], button_2["bg"], button_2["fg"] = text1, bg1, fg1
        button_1["text"] = "    "

    def chess_board(win):
        for i in range(8):
            for j in range(8):
                bg_color = "white" if (i + j) % 2 == 0 else "#696969"
                frame = tk.Frame(win, width=100, height=100, bg=bg_color)
                frame.grid(row=i, column=j)
