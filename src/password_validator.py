import re


def is_valid_length(password):
    """Return True if password contains 8 to 20 characters."""
    if not isinstance(password, str):
        raise TypeError("password must be a string")
    return 8 <= len(password) <= 20


def has_uppercase(password):
    """Return True if password contains at least one uppercase letter."""
    if not isinstance(password, str):
        raise TypeError("password must be a string")
    return bool(re.search(r"[A-Z]", password))


def has_digit(password):
    """Return True if password contains at least one digit."""
    if not isinstance(password, str):
        raise TypeError("password must be a string")
    return bool(re.search(r"\d", password))


def has_special_character(password):
    """Return True if password contains a special character."""
    if not isinstance(password, str):
        raise TypeError("password must be a string")
    return bool(re.search(r"[^A-Za-z0-9]", password))


def is_strong_password(password):
    """Return True if password satisfies all security requirements."""
    return (
        is_valid_length(password)
        and has_uppercase(password)
        and has_digit(password)
        and has_special_character(password)
    )


def password_strength(password):
    """Return a simple password strength category."""
    if not is_valid_length(password):
        return "Weak"

    score = 0

    if has_uppercase(password):
        score += 1

    if has_digit(password):
        score += 1

    if has_special_character(password):
        score += 1

    if score == 3:
        return "Strong"
    elif score == 2:
        return "Medium"
    else:
        return "Weak"