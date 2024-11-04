import tkinter as tk

class BattleshipUI:
    def __init__(self, root, player_board, computer_board, player_ships, handle_guess):
        self.root = root
        self.player_board = player_board
        self.computer_board = computer_board
        self.player_ships = player_ships
        self.handle_guess = handle_guess

        self.player_buttons = []
        self.computer_buttons = []

        self.create_board("Player", 0, self.player_board, self.player_buttons, self.place_ship)
        self.create_board("Computer", len(player_board) + 1, self.computer_board, self.computer_buttons, self.guess_position)

    def create_board(self, title, col_offset, board, button_list, command):
        label = tk.Label(self.root, text=f"{title} Board", font=("Arial", 12))
        label.grid(row=0, column=col_offset, columnspan=len(board))

        for row in range(len(board)):
            button_row = []
            for col in range(len(board[row])):
                button = tk.Button(self.root, width=3, height=2, command=lambda r=row, c=col: command(r, c))
                button.grid(row=row + 1, column=col + col_offset)
                button_row.append(button)
            button_list.append(button_row)

    def place_ship(self, row, col):
        # Logic for placing ships on the player's board
        pass

    def guess_position(self, row, col):
        self.handle_guess(row, col)
