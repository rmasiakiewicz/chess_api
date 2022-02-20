import pytest

from app import Board
from app.figure import Figure, Queen, King, Bishop, Knight, Pawn, Rook


#  few test example, there should be more


def test_new_figure():
    king = King("a2", 1, Board())
    assert king.x == 0
    assert king.y == 6
    assert king._position == "a2"
    assert king._color == 1
    assert king._FIGURE_TYPE == "king"


def test_create_queen_from_parent_class():
    queen = Figure.create("queen", "a2", 1, Board())
    assert type(queen) == Queen
    assert queen.x == 0
    assert queen.y == 6
    assert queen._position == "a2"
    assert queen._color == 1
    assert queen._FIGURE_TYPE == "queen"


def test_invalid_subclass_type_when_creating_object_from_parent_class():
    with pytest.raises(ValueError):
        Figure.create("sword", "b1", 3, Board())


def test_invalid_color_type():
    with pytest.raises(ValueError):
        Figure.create("queen", "b1", 3, Board())


def test_invalid_field():
    with pytest.raises(ValueError):
        Figure.create("queen", "b111", 1, Board())


def test_king_moves():
    x = King("b4", 1, Board())
    assert x.list_available_moves() == ["a3", "a4", "a5", "b3", "b5", "c3", "c4", "c5"]


def test_king_moves_corner():
    x = King("a1", 1, Board())
    assert x.list_available_moves() == ["a2", "b1", "b2"]


def test_queen_moves():
    x = Queen("a1", 1, Board())
    assert x.list_available_moves() == [
        "a2",
        "a3",
        "a4",
        "a5",
        "a6",
        "a7",
        "a8",
        "b1",
        "b2",
        "c1",
        "c3",
        "d1",
        "d4",
        "e1",
        "e5",
        "f1",
        "f6",
        "g1",
        "g7",
        "h1",
        "h8",
    ]


def test_bishop_moves():
    x = Bishop("a1", 1, Board())
    assert x.list_available_moves() == ["b2", "c3", "d4", "e5", "f6", "g7", "h8"]


def test_knight_moves():
    x = Knight("a1", 1, Board())
    assert x.list_available_moves() == ["b3", "c2"]


def test_white_pawn_moves_first_move():
    x = Pawn("a2", 1, Board())
    assert x.list_available_moves() == ["a3", "a4"]


def test_black_pawn_moves_first_move():
    x = Pawn("a7", 2, Board())
    assert x.list_available_moves() == ["a5", "a6"]


def test_white_pawn_moves_not_first_move():
    x = Pawn("a7", 1, Board())
    assert x.list_available_moves() == ["a8"]


def test_black_pawn_moves_not_first_move():
    x = Pawn("a6", 2, Board())
    assert x.list_available_moves() == ["a5"]


def test_rook_move():
    x = Rook("a1", 1, Board())
    assert x.list_available_moves() == [
        "a2",
        "a3",
        "a4",
        "a5",
        "a6",
        "a7",
        "a8",
        "b1",
        "c1",
        "d1",
        "e1",
        "f1",
        "g1",
        "h1",
    ]


def test_king_valid_move():
    x = King("a1", 1, Board())
    assert x.validate_move("a2") is True


def test_king_invalid_move():
    x = King("a1", 1, Board())
    assert x.validate_move("a7") is False
