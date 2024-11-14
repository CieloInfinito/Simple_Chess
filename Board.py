class Board:
    def __init__(self):
        # Initialize an 8x8 board with None
        self.grid = [[None for _ in range(8)] for _ in range(8)]

    def set_piece(self, piece, position):
        """Places a piece at a specified position on the board."""
        row, col = self._position_to_index(position)
        self.grid[row][col] = piece
        piece.position = position

    def get_piece(self, position):
        """Gets the piece at a specified position on the board."""
        row, col = self._position_to_index(position)
        return self.grid[row][col]

    def _position_to_index(self, position):
        """Converts a chess position (e.g., 'a1') to board indices (row, col)."""
        col = ord(position[0]) - ord('a')
        row = 8 - int(position[1])  # Converts '1'-'8' to 7-0
        return row, col

    def __repr__(self):
        """String representation of the board for easy visualization."""
        display = ""
        for row in self.grid:
            display += " ".join([str(piece) if piece else '.' for piece in row]) + "\n"
        return display
    
    def refresh_board(self, white_pieces, black_pieces):
        """
        Updates the board with the current pieces' positions from an array of pieces.

        Args:
            pieces_array (list): A list of Piece instances to place on the board.
        """
        # Clear the board
        self.grid = [[None for _ in range(8)] for _ in range(8)]
        
        # Place each piece in its specified position
        for piece in white_pieces:
            self.set_piece(piece, piece.position)

        for piece in black_pieces:
            self.set_piece(piece, piece.position)