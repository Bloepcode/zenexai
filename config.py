from dataclasses import dataclass

@dataclass
class ChessBoard:
    tl: tuple
    tr: tuple
    br: tuple
    bl: tuple

@dataclass
class Config:
    chess_board: ChessBoard
    minimum_change: float
