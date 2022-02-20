from itertools import chain
from typing import List, Tuple

from app.board import COORDINATES_TO_FIELDS


def move_coordinates_by_deltas(current_x: int, current_y: int, deltas: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    new_coordinates = []
    for delta in deltas:
        new_coordinates.append((current_x + delta[0], current_y + delta[1]))
    return new_coordinates


def get_diagonals(x: int, y: int, board_size: int) -> List[Tuple[int, int]]:
    return list(
        chain(
            zip(range(x - 1, -1, -1), range(y - 1, -1, -1)),
            zip(range(x + 1, board_size, 1), range(y + 1, board_size, 1)),
            zip(range(x + 1, board_size, 1), range(y - 1, -1, -1)),
            zip(range(x - 1, -1, -1), range(y + 1, board_size, 1)),
        )
    )


def get_verticals(x: int, y: int, board_size: int) -> List[Tuple[int, int]]:
    return list(
        chain(
            list(map(lambda new_y: (x, new_y), range(y + 1, board_size, 1))),
            list(map(lambda new_y: (x, new_y), range(y - 1, -1, -1))),
        )
    )


def get_horizontals(x: int, y: int, board_size: int) -> List[Tuple[int, int]]:
    return list(
        chain(
            list(map(lambda new_x: (new_x, y), range(x + 1, board_size, 1))),
            list(map(lambda new_x: (new_x, y), range(x - 1, -1, -1))),
        )
    )


def change_multiple_coordinates_to_fields(coordinates_list: List[Tuple[int, int]]) -> List[str]:
    return sorted([change_coordinates_to_field(coordinates) for coordinates in coordinates_list])


def change_coordinates_to_field(coordinates: Tuple[int, int]) -> str:
    return COORDINATES_TO_FIELDS.get(coordinates)
