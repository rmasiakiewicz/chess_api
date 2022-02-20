from abc import ABCMeta, abstractmethod
from itertools import product

from typing import List, Optional, Tuple

from app.board import Board, FIELDS_TO_COORDINATES
from app.utils import (
    move_coordinates_by_deltas,
    get_diagonals,
    get_verticals,
    get_horizontals,
    change_multiple_coordinates_to_fields,
)


FIGURES = ["king", "queen", "bishop", "rook", "knight", "pawn"]


class COLOR:
    WHITE = 1
    BLACK = 2

    AVAILABLE_COLORS = [WHITE, BLACK]

    TO_STR = {
        WHITE: "white",
        BLACK: "black",
    }


class Figure(object, metaclass=ABCMeta):
    _FIGURE_TYPE = None
    subclasses = {}

    @abstractmethod
    def __init__(self, position: str, color: int, board: Optional[Board]):
        if color not in COLOR.AVAILABLE_COLORS:
            raise ValueError("Unexpected color type. 1 == WHITE, 2 == BLACK")
        if FIELDS_TO_COORDINATES.get(position) is None:
            raise ValueError("Field doesn't exists")
        self._color = color
        self._position = position
        self._board = board

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses[cls._FIGURE_TYPE] = cls

    @classmethod
    def create(cls, figure_type: str, position: str, color: int, board: Optional[Board]):
        if figure_type not in cls.subclasses:
            raise ValueError("Bad figure type {}".format(figure_type))
        return cls.subclasses[figure_type](position, color, board)

    @property
    def x(self):
        coordinates = FIELDS_TO_COORDINATES.get(self._position)
        return coordinates[0]

    @property
    def y(self):
        coordinates = FIELDS_TO_COORDINATES.get(self._position)
        return coordinates[1]

    @abstractmethod
    def list_available_moves(self) -> List[str]:
        pass

    def validate_move(self, destination_field: str) -> bool:
        return True if destination_field in self.list_available_moves() else False


class King(Figure):
    _FIGURE_TYPE = "king"

    def __init__(self, position: str, color: int, board: Optional[Board]):
        super().__init__(position, color, board)

    def list_available_moves(self) -> List[str]:
        deltas = self._get_deltas()
        return change_multiple_coordinates_to_fields(
            self._board.validate_moves(move_coordinates_by_deltas(self.x, self.y, deltas))
        )

    @staticmethod
    def _get_deltas():
        return [(-1, 1), (-1, -1), (-1, 0), (1, 1), (1, -1), (1, 0), (0, 1), (0, -1)]


class Queen(Figure):
    _FIGURE_TYPE = "queen"

    def __init__(self, position: str, color: int, board: Optional[Board]):
        super().__init__(position, color, board)

    def list_available_moves(self) -> List[str]:
        return change_multiple_coordinates_to_fields(
            get_diagonals(self.x, self.y, self._board.size)
            + get_verticals(self.x, self.y, self._board.size)
            + get_horizontals(self.x, self.y, self._board.size)
        )


class Rook(Figure):
    _FIGURE_TYPE = "rook"

    def __init__(self, position: str, color: int, board: Optional[Board]):
        super().__init__(position, color, board)

    def list_available_moves(self) -> List[str]:
        return change_multiple_coordinates_to_fields(
            get_verticals(self.x, self.y, self._board.size) + get_horizontals(self.x, self.y, self._board.size)
        )


class Bishop(Figure):
    _FIGURE_TYPE = "bishop"

    def __init__(self, position: str, color: int, board: Optional[Board]):
        super().__init__(position, color, board)

    def list_available_moves(self) -> List[str]:
        return change_multiple_coordinates_to_fields(get_diagonals(self.x, self.y, self._board.size))


class Knight(Figure):
    _FIGURE_TYPE = "knight"

    def __init__(self, position: str, color: int, board: Optional[Board]):
        super().__init__(position, color, board)

    def list_available_moves(self) -> List[str]:
        deltas = self._get_deltas()
        return change_multiple_coordinates_to_fields(
            self._board.validate_moves(move_coordinates_by_deltas(self.x, self.y, deltas))
        )

    @staticmethod
    def _get_deltas() -> List[Tuple[int, int]]:
        return list(product([-1, 1], [-2, 2])) + list(product([-2, 2], [-1, 1]))


class Pawn(Figure):
    _FIGURE_TYPE = "pawn"

    def __init__(self, position: str, color: int, board: Optional[Board]):
        super().__init__(position, color, board)

    def list_available_moves(self) -> List[str]:
        deltas = self._get_deltas()
        return change_multiple_coordinates_to_fields(
            self._board.validate_moves(move_coordinates_by_deltas(self.x, self.y, deltas))
        )

    def _get_deltas(self) -> List[Tuple[int, int]]:
        if self._color == COLOR.WHITE and not self._is_moved():
            deltas = [(0, -1), (0, -2)]
        elif self._color == COLOR.WHITE:
            deltas = [(0, -1)]
        elif self._color == COLOR.BLACK and not self._is_moved():
            deltas = [(0, 1), (0, 2)]
        elif self._color == COLOR.BLACK:
            deltas = [(0, 1)]
        else:
            raise ValueError
        return deltas

    def _is_moved(self) -> bool:
        if (self._color == COLOR.WHITE and "2" in self._position) or (
            self._color == COLOR.BLACK and "7" in self._position
        ):
            return False
        else:
            return True
