from src.lambda_function import lambda_handler
import json


def test_lambda_handler():
    # Arrange
    event = {}
    context = {}
    expected_status_code = 200
    expected_body = 'Hello from Lambda - this is Roey!'

    # Act
    response = lambda_handler(event, context)

    # Assert
    assert response['statusCode'] == expected_status_code
    assert json.loads(response['body']) == expected_body

