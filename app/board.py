from typing import List, Tuple

FIELDS_TO_COORDINATES = {
    "a1": (0, 7),
    "b1": (1, 7),
    "c1": (2, 7),
    "d1": (3, 7),
    "e1": (4, 7),
    "f1": (5, 7),
    "g1": (6, 7),
    "h1": (7, 7),
    "a2": (0, 6),
    "b2": (1, 6),
    "c2": (2, 6),
    "d2": (3, 6),
    "e2": (4, 6),
    "f2": (5, 6),
    "g2": (6, 6),
    "h2": (7, 6),
    "a3": (0, 5),
    "b3": (1, 5),
    "c3": (2, 5),
    "d3": (3, 5),
    "e3": (4, 5),
    "f3": (5, 5),
    "g3": (6, 5),
    "h3": (7, 5),
    "a4": (0, 4),
    "b4": (1, 4),
    "c4": (2, 4),
    "d4": (3, 4),
    "e4": (4, 4),
    "f4": (5, 4),
    "g4": (6, 4),
    "h4": (7, 4),
    "a5": (0, 3),
    "b5": (1, 3),
    "c5": (2, 3),
    "d5": (3, 3),
    "e5": (4, 3),
    "f5": (5, 3),
    "g5": (6, 3),
    "h5": (7, 3),
    "a6": (0, 2),
    "b6": (1, 2),
    "c6": (2, 2),
    "d6": (3, 2),
    "e6": (4, 2),
    "f6": (5, 2),
    "g6": (6, 2),
    "h6": (7, 2),
    "a7": (0, 1),
    "b7": (1, 1),
    "c7": (2, 1),
    "d7": (3, 1),
    "e7": (4, 1),
    "f7": (5, 1),
    "g7": (6, 1),
    "h7": (7, 1),
    "a8": (0, 0),
    "b8": (1, 0),
    "c8": (2, 0),
    "d8": (3, 0),
    "e8": (4, 0),
    "f8": (5, 0),
    "g8": (6, 0),
    "h8": (7, 0),
}


COORDINATES_TO_FIELDS = {v: k for k, v in FIELDS_TO_COORDINATES.items()}


class Board:
    def __init__(self):
        self._size = 8
        self._fields = [[" "] * self._size for _ in range(self._size)]

    @property
    def size(self):
        return self._size

    def validate_moves(self, moves: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        return [(x, y) for x, y in moves if 0 <= x < self.size and 0 <= y < self.size]
