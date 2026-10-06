# tests/test_validator.py
from validator import validate_email, validate_phone


def test_validate_email():
    assert validate_email("test@example.com") is True
    assert validate_email("invalid") is False


def test_validate_phone():
    assert validate_phone("+7 (999) 123-45-67") is True
    assert validate_phone("8 999 123 45 67") is True
    assert validate_phone("+7 495 123-45-67") is False
    assert validate_phone("not-a-phone") is False
