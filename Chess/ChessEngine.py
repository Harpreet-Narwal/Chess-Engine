class GameState():
    def __init__(self):
        
        # borad is 8x8 2d list, each element of the list has 2 characters.
        # The first character represents the color of piece 'b' or 'w'
        # The secon character represents the type of pieces, 'K', 'Q', 'R', 'B', 'N', or 'p'
        # "--" represents an empty space with no piece.

        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]

        ]
        self.whiteToMove = True
        self.moveLog = []
