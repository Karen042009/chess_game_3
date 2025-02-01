import tkinter as tk
import board
from abc import ABC, abstractmethod
class Piece(ABC):
    @abstractmethod
    def valid_move(self, start, end):
        return False
class Knight(Piece):
    def valid_move(self, start, end):
        dx = abs(start[0] - end[0])
        dy = abs(start[1] - end[1])
        return (dx == 2 and dy == 1) or (dx == 1 and dy == 2)
class Queen(Piece):
    def valid_move(self, start, end):
        dx = abs(start[0] - end[0])
        dy = abs(start[1] - end[1])
        return dx == dy or start[0] == end[0] or start[1] == end[1]
class King(Piece):
    def valid_move(self, start, end):
        dx = abs(start[0] - end[0])
        dy = abs(start[1] - end[1])
        return dx <= 1 and dy <= 1
class Rook(Piece):
    def valid_move(self, start, end):
        return start[0] == end[0] or start[1] == end[1]
class Bishop(Piece):
    def valid_move(self, start, end):
        dx = abs(start[0] - end[0])
        dy = abs(start[1] - end[1])
        return dx == dy
class Pawn(Piece):
    def valid_move(self, start, end):
        return True
class_board_button = board.Board_button()
def piece(win):
    # սպիտակ զինվոր
    btn_1 = tk.Button(win,text="♙",font=("Arial", 25),bg="white",fg="black",bd=0,command=lambda: class_board_button.butto(1, btn_1),)
    btn_1.grid(row=6, column=0)
    btn_2 = tk.Button(win,text="♙",font=("Arial", 25),bg="#696969",fg="black",bd=0,command=lambda: class_board_button.butto(1, btn_2),)
    btn_2.grid(row=6, column=1)
    btn_3 = tk.Button(win,text="♙",font=("Arial", 25),bg="white",fg="black",bd=0,command=lambda: class_board_button.butto(btn_3),)
    btn_3.grid(row=6, column=2)
    btn_4 = tk.Button(win,text="♙",font=("Arial", 25),bg="#696969",fg="black",bd=0,command=lambda: class_board_button.butto(btn_4),)
    btn_4.grid(row=6, column=3)
    btn_5 = tk.Button(win,text="♙",font=("Arial", 25),bg="white",fg="black",bd=0,command=lambda: class_board_button.butto(btn_5),)
    btn_5.grid(row=6, column=4)
    btn_6 = tk.Button(win,text="♙",font=("Arial", 25),bg="#696969",fg="black",bd=0,command=lambda: class_board_button.butto(btn_6),)
    btn_6.grid(row=6, column=5)
    btn_7 = tk.Button(win,text="♙",font=("Arial", 25),bg="white",fg="black",bd=0,command=lambda: class_board_button.butto(btn_7),)
    btn_7.grid(row=6, column=6)
    btn_8 = tk.Button(win,text="♙",font=("Arial", 25),bg="#696969",fg="black",bd=0,command=lambda: class_board_button.butto(btn_8),)
    btn_8.grid(row=6, column=7)
    # սև զինվոր
    btn_9 = tk.Button(win,text="♟",font=("Arial", 25),bg="#696969",fg="black",bd=0,command=lambda: class_board_button.butto(btn_9),)
    btn_9.grid(row=1, column=0)
    btn_10 = tk.Button(win,text="♟",font=("Arial", 25),bg="white",fg="black",bd=0,command=lambda: class_board_button.butto(btn_10),)
    btn_10.grid(row=1, column=1)
    btn_12 = tk.Button(win,text="♟",font=("Arial", 25),bg="#696969",fg="black",bd=0,command=lambda: class_board_button.butto(btn_12),)
    btn_12.grid(row=1, column=2)
    btn_13 = tk.Button(win,text="♟",font=("Arial", 25),bg="white",fg="black",bd=0,command=lambda: class_board_button.butto(btn_13),)
    btn_13.grid(row=1, column=3)
    btn_14 = tk.Button(win,text="♟",font=("Arial", 25),bg="#696969",fg="black",bd=0,command=lambda: class_board_button.butto(btn_14),)
    btn_14.grid(row=1, column=4)
    btn_15 = tk.Button(win,text="♟",font=("Arial", 25),bg="white",fg="black",bd=0,command=lambda: class_board_button.butto(btn_15),)
    btn_15.grid(row=1, column=5)
    btn_16 = tk.Button(win,text="♟",font=("Arial", 25),bg="#696969",fg="black",bd=0,command=lambda: class_board_button.butto(btn_16),)
    btn_16.grid(row=1, column=6)
    btn_17 = tk.Button(win,text="♟",font=("Arial", 25),bg="white",fg="black",bd=0,command=lambda: class_board_button.butto(btn_17),)
    btn_17.grid(row=1, column=7)
    # սև թագուհի
    btn_18 = tk.Button(win,text="♛",font=("Arial", 25),bg="#696969",fg="black",bd=0,command=lambda: class_board_button.butto(btn_18),)
    btn_18.grid(row=0, column=3)
    # սպիտակ թագուհի
    btn_19 = tk.Button(win,text="♕",font=("Arial", 25),bg="white",fg="black",bd=0,command=lambda: class_board_button.butto(btn_19),)
    btn_19.grid(row=7, column=3)
    # սև նավ ♜
    btn_20 = tk.Button(win,text="♜",font=("Arial", 25),bg="white",fg="black",bd=0,command=lambda: class_board_button.butto(btn_20),)
    btn_20.grid(row=0, column=0)
    btn_21 = tk.Button(win,text="♜",font=("Arial", 25),bg="#696969",fg="black",bd=0,command=lambda: class_board_button.butto(btn_21),)
    btn_21.grid(row=0, column=7)
    # սպիտակ նավ ♜
    btn_22 = tk.Button(win,text="♖",font=("Arial", 25),bg="#696969",fg="black",bd=0,command=lambda: class_board_button.butto(btn_22),)
    btn_22.grid(row=7, column=0)
    btn_23 = tk.Button(win,text="♖",font=("Arial", 25),bg="white",fg="black",bd=0,command=lambda: class_board_button.butto(btn_23),)
    btn_23.grid(row=7, column=7)
    # սև ձի ♞
    btn_24 = tk.Button(win,text="♞",font=("Arial", 25),bg="#696969",fg="black",bd=0,command=lambda: class_board_button.butto(btn_24))
    btn_24.grid(row=0, column=1)
    btn_25 = tk.Button(win,text="♞",font=("Arial", 25),bg="white",fg="black",bd=0,command=lambda: class_board_button.butto(btn_25),)
    btn_25.grid(row=0, column=6)
    # սպիտակ ձի ♘
    btn_26 = tk.Button(win,text="♘",font=("Arial", 25),bg="white",fg="black",bd=0,command=lambda: class_board_button.butto(btn_26),)
    btn_26.grid(row=7, column=1)
    btn_27 = tk.Button(win,text="♘",font=("Arial", 25),bg="#696969",fg="black",bd=0,command=lambda: class_board_button.butto(btn_27),)
    btn_27.grid(row=7, column=6)
    # սև ♝
    btn_28 = tk.Button(win,text="♝",font=("Arial", 25),bg="white",fg="black",bd=0,command=lambda: class_board_button.butto(btn_28),)
    btn_28.grid(row=0, column=2)
    btn_29 = tk.Button(win,text="♝",font=("Arial", 25),bg="#696969",fg="black",bd=0,command=lambda: class_board_button.butto(btn_29),)
    btn_29.grid(row=0, column=5)
    # սպիտակ ♗
    btn_30 = tk.Button(win,text="♗",font=("Arial", 25),bg="#696969",fg="black",bd=0,command=lambda: class_board_button.butto(btn_30),)
    btn_30.grid(row=7, column=2)
    btn_300 = tk.Button(win,text="♗",font=("Arial", 25),bg="white",fg="black",bd=0,command=lambda: class_board_button.butto(btn_300),)
    btn_300.grid(row=7, column=5)
    # սև թագավոր  ♚
    btn_31 = tk.Button(win,text="♚",font=("Arial", 25),bg="white",fg="black",bd=0,command=lambda: class_board_button.butto(btn_31),)
    btn_31.grid(row=0, column=4)
    # սպիտակ թագավոր ♔
    btn_32 = tk.Button(win,text="♔",font=("Arial", 25),bg="#696969",fg="black",bd=0,command=lambda: class_board_button.butto(btn_32),)
    btn_32.grid(row=7, column=4)
    btn_33 = tk.Button(win,text="    ",font=("Arial", 25),bg="white",fg="black",bd=0,command=lambda: class_board_button.butto(btn_33),)
    btn_33.grid(row=2, column=0)
    btn_34 = tk.Button(win,text="    ",font=("Arial", 25),bg="#696969",fg="black",bd=0,command=lambda: class_board_button.butto(btn_34),)
    btn_34.grid(row=3, column=0)
    btn_35 = tk.Button(win,text="    ",font=("Arial", 25),bg="white",fg="black",bd=0,command=lambda: class_board_button.butto(btn_35),)
    btn_35.grid(row=4, column=0)
    btn_36 = tk.Button(win,text="    ",font=("Arial", 25),bg="#696969",fg="black",bd=0,command=lambda: class_board_button.butto(btn_36),)
    btn_36.grid(row=5, column=0)
    btn_37 = tk.Button(win,text="    ",font=("Arial", 25),bg="#696969",fg="black",bd=0,command=lambda: class_board_button.butto(btn_37),)
    btn_37.grid(row=2, column=1)
    btn_38 = tk.Button(win,text="    ",font=("Arial", 25),bg="white",fg="black",bd=0,command=lambda: class_board_button.butto(btn_38),)
    btn_38.grid(row=3, column=1)
    btn_39 = tk.Button(win,text="    ",font=("Arial", 25),bg="#696969",fg="black",bd=0,command=lambda: class_board_button.butto(btn_39),)
    btn_39.grid(row=4, column=1)
    btn_40 = tk.Button(win,text="    ",font=("Arial", 25),bg="white",fg="black",bd=0,command=lambda: class_board_button.butto(btn_40),)
    btn_40.grid(row=5, column=1)
    btn_41 = tk.Button(win,text="    ",font=("Arial", 25),bg="#696969",fg="black",bd=0,command=lambda: class_board_button.butto(btn_41),)
    btn_41.grid(row=2, column=3)
    btn_42 = tk.Button(win,text="    ",font=("Arial", 25),bg="white",fg="black",bd=0,command=lambda: class_board_button.butto(btn_42),)
    btn_42.grid(row=3, column=3)
    btn_43 = tk.Button(win,text="    ",font=("Arial", 25),bg="#696969",fg="black",bd=0,command=lambda: class_board_button.butto(btn_43),)
    btn_43.grid(row=4, column=3)
    btn_44 = tk.Button(win,text="    ",font=("Arial", 25),bg="white",fg="black",bd=0,command=lambda: class_board_button.butto(btn_44),)
    btn_44.grid(row=5, column=3)
    btn_45 = tk.Button(win,text="    ",font=("Arial", 25),bg="white",fg="black",bd=0,command=lambda: class_board_button.butto(btn_45),)
    btn_45.grid(row=2, column=4)
    btn_46 = tk.Button(win,text="    ",font=("Arial", 25),bg="#696969",fg="black",bd=0,command=lambda: class_board_button.butto(btn_46),)
    btn_46.grid(row=3, column=4)
    btn_47 = tk.Button(win,text="    ",font=("Arial", 25),bg="white",fg="black",bd=0,command=lambda: class_board_button.butto(btn_47),)
    btn_47.grid(row=4, column=4)
    btn_48 = tk.Button(win,text="    ",font=("Arial", 25),bg="#696969",fg="black",bd=0,command=lambda: class_board_button.butto(btn_48),)
    btn_48.grid(row=5, column=4)
    btn_49 = tk.Button(win,text="    ",font=("Arial", 25),bg="#696969",fg="black",bd=0,command=lambda: class_board_button.butto(btn_49),)
    btn_49.grid(row=2, column=5)
    btn_50 = tk.Button(win,text="    ",font=("Arial", 25),bg="white",fg="black",bd=0,command=lambda: class_board_button.butto(btn_50),)
    btn_50.grid(row=3, column=5)
    btn_51 = tk.Button(win,text="    ",font=("Arial", 25),bg="#696969",fg="black",bd=0,command=lambda: class_board_button.butto(btn_51),)
    btn_51.grid(row=4, column=5)
    btn_52 = tk.Button(win,text="    ",font=("Arial", 25),bg="white",fg="black",bd=0,command=lambda: class_board_button.butto(btn_52),)
    btn_52.grid(row=5, column=5)
    btn_53 = tk.Button(win,text="    ",font=("Arial", 25),bg="white",fg="black",bd=0,command=lambda: class_board_button.butto(btn_53),)
    btn_53.grid(row=2, column=6)
    btn_54 = tk.Button(win,text="    ",font=("Arial", 25),bg="#696969",fg="black",bd=0,command=lambda: class_board_button.butto(btn_54),)
    btn_54.grid(row=3, column=6)
    btn_55 = tk.Button(win,text="    ",font=("Arial", 25),bg="white",fg="black",bd=0,command=lambda: class_board_button.butto(btn_55),)
    btn_55.grid(row=4, column=6)
    btn_56 = tk.Button(win,text="    ",font=("Arial", 25),bg="#696969",fg="black",bd=0,command=lambda: class_board_button.butto(btn_56),)
    btn_56.grid(row=5, column=6)
    btn_57 = tk.Button(win,text="    ",font=("Arial", 25),bg="#696969",fg="black",bd=0,command=lambda: class_board_button.butto(btn_57),)
    btn_57.grid(row=2, column=7)
    btn_58 = tk.Button(win,text="    ",font=("Arial", 25),bg="white",fg="black",bd=0,command=lambda: class_board_button.butto(btn_58),)
    btn_58.grid(row=3, column=7)
    btn_59 = tk.Button(win,text="    ",font=("Arial", 25),bg="#696969",fg="black",bd=0,command=lambda: class_board_button.butto(btn_59),)
    btn_59.grid(row=4, column=7)
    btn_60 = tk.Button(win,text="    ",font=("Arial", 25),bg="white",fg="black",bd=0,command=lambda: class_board_button.butto(btn_60),)
    btn_60.grid(row=5, column=7)
    btn_61 = tk.Button(win,text="    ",font=("Arial", 25),bg="white",fg="black",bd=0,command=lambda: class_board_button.butto(btn_61),)
    btn_61.grid(row=2, column=2)
    btn_62 = tk.Button(win,text="    ",font=("Arial", 25),bg="#696969",fg="black",bd=0,command=lambda: class_board_button.butto(btn_62),)
    btn_62.grid(row=3, column=2)
    btn_63 = tk.Button(win,text="    ",font=("Arial", 25),bg="white",fg="black",bd=0,command=lambda: class_board_button.butto(btn_63),)
    btn_63.grid(row=4, column=2)
    btn_64 = tk.Button(win,text="    ",font=("Arial", 25),bg="#696969",fg="black",bd=0,command=lambda: class_board_button.butto(btn_64),)
    btn_64.grid(row=5, column=2)
def move_(s_x, s_y, f_x, f_y):
    global board_matrix
    board_matrix[s_x][s_y], board_matrix[f_x][f_y] = board_matrix[f_x][f_y], board_matrix[s_x][s_y]
    board_matrix[s_x][s_y] = " "
    return board_matrix
board_matrix = [["♜", "♞", "♝", "♚", "♛", "♝", "♞", "♜"],["♟", "♟", "♟", "♟", "♟", "♟", "♟", "♟"],[" ", " ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " ", " "],["♙", "♙", "♙", "♙", "♙", "♙", "♙", "♙"],["♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"],]
def cek_move(a1,a2,b1, b2):
    global board_matrix
    b = board.Board_move()
    flag = False
    if board_matrix[a1][a2] == "♙" or board_matrix[a1][a2] == "♟":
        ss = Pawn()
        if ss.valid_move([a1,a2], [b1,b2]):
            board_matrix = move_(a1, a2, b1, b2)
            flag = True
    elif board_matrix[a1][a2] == "♘" or board_matrix[a1][a2] == "♞":
        ss = Knight()
        if ss.valid_move([a1,a2], [b1,b2]):
            board_matrix = move_(a1, a2, b1, b2)
            flag = True
    elif board_matrix[a1][a2] == "♕" or board_matrix[a1][a2] == "♛":
        ss = Queen()
        if ss.valid_move([a1,a2], [b1,b2]):
            board_matrix = move_(a1, a2, b1, b2)
            flag = True
    elif board_matrix[a1][a2] == "♔" or board_matrix[a1][a2] == "♔":
        ss = King()
        if ss.valid_move([a1,a2], [b1,b2]):
            board_matrix = move_(a1, a2, b1, b2)
            flag = True
    elif board_matrix[a1][a2] == "♗" or board_matrix[a1][a2] == "♝":
        ss = Bishop()
        if ss.valid_move([a1,a2], [b1,b2]):
            board_matrix = move_(a1, a2, b1, b2)
            flag = True
    elif board_matrix[a1][a2] == "♖" or board_matrix[a1][a2] == "♜":
        ss = Rook()
        if ss.valid_move([a1,a2], [b1,b2]):
            board_matrix = move_(a1, a2, b1, b2)
            flag = True
    else:
        flag = False
    if flag:
        return True
    else:
        return False
def g():
    win = tk.Tk()
    a = board.Board
    a.chess_board(win)
    piece(win)
    win.mainloop()