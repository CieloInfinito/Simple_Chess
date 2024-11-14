from Piece import Piece
from Board import Board

# Create the Board instance
board = Board()
# Crear listas de piezas blancas y negras
white_pieces = [
    [Piece("king", "white", "e1")],                # King
    [Piece("queen", "white", "d1")],               # Queen
    [Piece("rook", "white", "a1"), Piece("rook", "white", "h1")],       # Rooks
    [Piece("knight", "white", "b1"), Piece("knight", "white", "g1")],   # Knights
    [Piece("bishop", "white", "c1"), Piece("bishop", "white", "f1")],   # Bishops
    [Piece("pawn", "white", f"{chr(97 + i)}2") for i in range(8)]       # Pawns
]

black_pieces = [
    [Piece("king", "black", "e8")],                # King
    [Piece("queen", "black", "d8")],               # Queen
    [Piece("rook", "black", "a8"), Piece("rook", "black", "h8")],       # Rooks
    [Piece("knight", "black", "b8"), Piece("knight", "black", "g8")],   # Knights
    [Piece("bishop", "black", "c8"), Piece("bishop", "black", "f8")],   # Bishops
    [Piece("pawn", "black", f"{chr(97 + i)}7") for i in range(8)]       # Pawns
]

# Función para imprimir todas las piezas en un array de piezas
def print_pieces(pieces, color):
    print(f"{color.capitalize()} pieces:")
    piece_names = ["King", "Queen", "Rooks", "Knights", "Bishops", "Pawns"]
    for name, piece_list in zip(piece_names, pieces):
        for piece in piece_list:
            print(f"{name}: {piece.info()}")


board.refresh_board(white_pieces, black_pieces)
print("-----------------------")
print(board)
