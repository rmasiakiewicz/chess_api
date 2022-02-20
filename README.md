# chess_api
Simple rest app that helps chess game. You can use two endpoints.
1. /api/v1/<chess_figure>/<color>/<current_field> - gives all possible moves for a given figure assuming the board is empty
2. /api/v1/<chess_figure>/<color>/<current_field>/<destination_field> - validate if move is possible

expected chess figures names - king, queen, bishop, rook, knight, pawn
expected colors - 1 (WHITE), 2 (BLACK)
expected fields - everything that match this regex ^[a-h]{1}[1-8]{1}$

Unittests are not complete. I just wrote a few examples.

HOW TO RUN APP:
1. Download repository
2. Install dependencies from requirements.txt
3. Type flask run (from root repo directory)

HOW TO RUN TESTS:
From root repo directory type: pytest tests/

LINTER AND FORMATTER:
linter on demand - sh scripts/style_checker.sh
formatter - sh scripts/format_code.sh

PRE-PUSH LINTER:
Please copy contents of the file scripts/style_checker.sh to .git/hooks/pre-push
Then make sure that .git/hooks/pre-push is executable (chmod +x)
