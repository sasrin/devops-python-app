import pytest
import app

def test_logging():
    with open('app.log', 'r') as log_file:
        assert "Hello, DevOps!" in log_file.read()
