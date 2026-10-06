# validator.py
def validate_email(email: str) -> bool:
    """Валидация email-адреса."""
    import re
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))


def validate_phone(phone: str) -> bool:
    """Проверяет номер российского мобильного телефона."""
    import re

    cleaned = re.sub(r'[\s()-]', '', phone)
    return bool(re.fullmatch(r'(?:\+7|8)9\d{9}', cleaned))


def validate_snils(snils: str) -> bool:
    """Валидация СНИЛС по формату и контрольному числу."""
    import re

    cleaned = re.sub(r'[-\s]', '', snils)
    if not re.fullmatch(r'\d{11}', cleaned):
        return False

    numbers = [int(digit) for digit in cleaned[:9]]
    check_sum = int(cleaned[9:])
    calculated = sum((9 - index) * digit for index, digit in enumerate(numbers))

    if calculated < 100:
        expected = calculated
    elif calculated % 101 == 100:
        expected = 0
    else:
        expected = calculated % 101

    return expected == check_sum

