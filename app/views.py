import json
from http import HTTPStatus

from flask import Blueprint

from app import board
from app.board import FIELDS_TO_COORDINATES
from app.figure import FIGURES, COLOR, Figure

blueprint = Blueprint("general", __name__)


@blueprint.route("/api/v1/<string:chess_figure>/<int:color>/<string:current_field>", methods=["GET"])
def list_available_moves(chess_figure, color, current_field):
    json_response = {
        "availableMoves": [],
        "error": None,
        "figure": chess_figure,
        "color": COLOR.TO_STR.get(color),
        "currentField": current_field,
    }
    valid_request, json_response, status = validate_request(chess_figure, color, current_field, json_response)
    if not valid_request:
        return json.dumps(json_response), status
    figure = Figure.create(chess_figure, current_field, color, board)
    json_response["availableMoves"] = figure.list_available_moves()
    return json.dumps(json_response), status


@blueprint.route(
    "/api/v1/<string:chess_figure>/<int:color>/<string:current_field>/<string:destination_field>", methods=["GET"]
)
def validate_move(chess_figure, color, current_field, destination_field):
    json_response = {
        "move": None,
        "figure": chess_figure,
        "color": COLOR.TO_STR.get(color),
        "error": None,
        "currentField": current_field,
        "destField": destination_field,
    }
    valid_request, json_response, status = validate_request(
        chess_figure, color, current_field, json_response, destination_field
    )
    if not valid_request:
        return json.dumps(json_response), status
    figure = Figure.create(chess_figure, current_field, color, board)
    if figure.validate_move(destination_field):
        json_response["move"] = "valid"
        status = HTTPStatus.OK
    else:
        json_response["move"] = "invalid"
        json_response["error"] = "Current move is not permitted."
        status = HTTPStatus.CONFLICT
    return json.dumps(json_response), status


def validate_request(figure, color, current_field, json_response, destination_field=None):
    if figure not in FIGURES:
        json_response["error"] = "Figure does not exist."
        return False, json_response, HTTPStatus.BAD_REQUEST
    if color not in COLOR.AVAILABLE_COLORS:
        json_response["error"] = "Color does not exist."
        return False, json_response, HTTPStatus.BAD_REQUEST
    if FIELDS_TO_COORDINATES.get(current_field) is None or (
        destination_field is not None and FIELDS_TO_COORDINATES.get(destination_field) is None
    ):
        json_response["error"] = "Field does not exist."
        return False, json_response, HTTPStatus.BAD_REQUEST
    else:
        return True, json_response, HTTPStatus.OK
