import pytest
from app import get_message

def test_get_message():
    assert get_message() == "Hello, DevOps!"