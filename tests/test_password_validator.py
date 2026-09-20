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
    assert result == True


def test_password_strength_medium():
    password = "Password1"
    result = password_strength(password)
    assert result == "Medium"

def test_uppercase_false():
    assert has_uppercase("password123") == False


def test_digit_true():
    assert has_digit("Password1") == True


def test_special_character_false():
    assert has_special_character("Password1") == False


def test_strong_password_false():
    assert is_strong_password("password1") == False


def test_password_strength_weak():
    assert password_strength("password") == "Weak"


def test_password_strength_strong():
    assert password_strength("Password1!") == "Strong"