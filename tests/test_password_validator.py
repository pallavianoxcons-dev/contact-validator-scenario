import pytest

from src.password_validator import (
    is_valid_length,
    has_uppercase,
    has_digit,
    has_special_character,
    is_strong_password,
    password_strength,
)


def test_valid_length():
    assert is_valid_length("Password1") == True


def test_invalid_length():
    assert is_valid_length("Pass1") == False


def test_uppercase():
    assert has_uppercase("Password1") == True


def test_digit():
    assert has_digit("Password") == False


def test_special_character():
    assert has_special_character("Password1!") == True


def test_type_error():
    with pytest.raises(TypeError):
        is_valid_length(12345)


def test_strong_password():
    password = "Password1!"
    result = is_strong_password(password)
    assert result == False


def test_password_strength_medium():
    password = "Password1"
    result = password_strength(password)
    assert result == "Medium"