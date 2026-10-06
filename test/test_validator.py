# tests/test_validator.py
from validator import validate_email, validate_phone, validate_snils


def test_validate_email():
    assert validate_email("test@example.com") is True
    assert validate_email("invalid") is False


def test_validate_phone():
    assert validate_phone("+7 (999) 123-45-67") is True
    assert validate_phone("8 999 123 45 67") is True
    assert validate_phone("+7 495 123-45-67") is False
    assert validate_phone("not-a-phone") is False


def test_validate_snils():
    assert validate_snils("11223344595") is True
    assert validate_snils("001-001-999 65") is True
    assert validate_snils("123") is False
    assert validate_snils("abcdefghijk") is False
    assert validate_snils("11223344500") is False
