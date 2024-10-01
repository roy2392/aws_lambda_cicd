from src.lambda_function import lambda_handler

def test_my_function():
    result = lambda_handler(5)
    expected = 25
    assert result == expected, f"Expected {expected}, got {result}"