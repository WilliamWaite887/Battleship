import tkinter as tk
from ships import Ship, is_valid_placement
from ui import BattleshipUI

# Constants
BOARD_SIZE = 10

# Create the main game logic
def main():
    player_board = [["~"] * BOARD_SIZE for _ in range(BOARD_SIZE)]
    computer_board = [["~"] * BOARD_SIZE for _ in range(BOARD_SIZE)]

    # Hash maps for tracking ship positions
    player_ships = {}
    computer_ships = {}

    # Create and place ships (example for computer)
    computer_ship = Ship("Carrier", 5)
    while True:
        start_row, start_col = 2, 2  # Randomly choose start coordinates
        orientation = 'H'  # Choose orientation
        positions = computer_ship.place_ship(start_row, start_col, orientation, BOARD_SIZE)
        if positions and is_valid_placement(computer_ships, positions):
            computer_ships.update(positions)
            break

    # Start the UI
    root = tk.Tk()
    ui = BattleshipUI(root, player_board, computer_board, player_ships, lambda r, c: print(f"Guessed: {r}, {c}"))
    root.mainloop()

if __name__ == "__main__":
    main()
