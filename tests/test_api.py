from app import create_app


def test_available_moves_endpoint_success():
    flask_app = create_app()
    with flask_app.test_client() as test_client:
        response = test_client.get("/api/v1/bishop/1/a1")
        assert response.status_code == 200
        assert b'"error": null' in response.data


def test_available_moves_endpoint_bad_field():
    flask_app = create_app()
    with flask_app.test_client() as test_client:
        response = test_client.get("/api/v1/bishop/1/a11")
        assert response.status_code == 400
        assert b"Field does not exist." in response.data


def test_available_moves_endpoint_bad_figure():
    flask_app = create_app()
    with flask_app.test_client() as test_client:
        response = test_client.get("/api/v1/sword/1/a11")
        assert response.status_code == 400
        assert b"Figure does not exist." in response.data


def test_validate_move_endpoint_valid_move():
    flask_app = create_app()
    with flask_app.test_client() as test_client:
        response = test_client.get("/api/v1/bishop/1/a1/b2")
        assert response.status_code == 200
        assert b'"move": "valid"' in response.data


def test_validate_move_endpoint_invalid_move():
    flask_app = create_app()
    with flask_app.test_client() as test_client:
        response = test_client.get("/api/v1/bishop/1/a1/a2")
        assert response.status_code == 409
        assert b'"move": "invalid"' in response.data


def test_validate_move_endpoint_bad_field():
    flask_app = create_app()
    with flask_app.test_client() as test_client:
        response = test_client.get("/api/v1/bishop/1/a1/a11")
        assert response.status_code == 400
        assert b"Field does not exist." in response.data
