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

