class Ship:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.positions = {}

    def place_ship(self, start_row, start_col, orientation, board_size):
        if orientation not in ['H', 'V']:
            raise ValueError("Invalid orientation. Use 'H' for horizontal or 'V' for vertical.")
        
        positions = {}
        if orientation == 'H':
            if start_col + self.size > board_size:
                return None  # Out of bounds
            for i in range(self.size):
                positions[(start_row, start_col + i)] = True
        else:
            if start_row + self.size > board_size:
                return None  # Out of bounds
            for i in range(self.size):
                positions[(start_row + i, start_col)] = True

        self.positions = positions
        return positions

def is_valid_placement(board_map, new_positions):
    for position in new_positions:
        if position in board_map:
            return False
    return True
