class Piece:
    PIECE_CODES = {
        "pawn": 1,
        "knight": 3,
        "bishop": 4,
        "rook": 5,
        "king": 8,
        "queen": 9
    }

    def __init__(self, piece_type: str, color: str, position: str):
        """
        Initializes a piece with type, color, starting position, and piece code.
        
        Args:
            piece_type (str): The type of the piece (e.g., 'pawn', 'rook').
            color (str): The color of the piece ('white' or 'black').
            position (str): The position on the board (e.g., 'a1', 'h8').
        """
        self.piece_type = piece_type
        self.color = color
        self.position = position
        # Assign piece_code based on the piece_type
        self.piece_code = self.PIECE_CODES.get(piece_type, 0)  # Default to 0 if type not found

    def __repr__(self):
        return f"{self.color.capitalize()} {self.piece_type.capitalize()} at {self.position}"

    def __str__(self):
        """Returns only the piece_type when printed."""
        return self.piece_type

    def info(self):
        """Returns a string with all attributes of the piece."""
        return (f"Type: {self.piece_type.capitalize()}, "
                f"Color: {self.color.capitalize()}, "
                f"Position: {self.position}, "
                f"Code: {self.piece_code}")
