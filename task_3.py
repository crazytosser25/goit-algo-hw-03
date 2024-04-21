import re

def normalize_phone(phone_number: str) -> str:
    """Normalizes a phone number string by adding the appropriate country code
    and removing non-digit characters.

    Args:
        phone_number (str): A string representing a phone number with or without country code.

    Returns:
        str: The normalized phone number in the format +380xxxxxxx
    """
    # Preparing pattern for checking presence of country code in phone number
    pattern: str = r'380\d{9}'
    # Removing all non-digit symbols
    sanitized_phone: str = re.sub(r'\D', '', phone_number)
    # Checking country code
    if re.search(pattern, sanitized_phone):
        # Adding + if country code is present
        sanitized_phone = '+' + sanitized_phone
    else:
        # Adding +38 if country code is absent
        sanitized_phone = '+38' + sanitized_phone
    # Returning sanitized phone number
    return sanitized_phone


# Test run
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
