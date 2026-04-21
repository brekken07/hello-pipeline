import pytest
from app import greet, add, multiply

def test_greet_normal():
    assert greet("Titi") == "Hello, Titi! Pipeline is alive 🚀"

def test_greet_empty_raises():
    with pytest.raises(ValueError):
        greet("")

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 99) == 0
