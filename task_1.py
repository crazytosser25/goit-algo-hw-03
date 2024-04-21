from datetime import datetime

def get_days_from_today(date: str) -> int:
    """Calculates and returns the number of days between a given date and today.
    Throws ValueError if the date format is not "YYYY-MM-DD".

    Args:
        date (str): A string representing a date in YYYY-MM-DD format.

    Returns:
        int: The number of days between the input date and today's date.
    """
    # Converting string to datetime format, living only date
    try:
        date: datetime = datetime.strptime(date, '%Y-%m-%d').date()
    # Returning error if string format is wrong
    except ValueError:
        return 'Date format must be "YYYY-MM-DD" only!!!'
    # Receiving today's date
    today: datetime = datetime.today().date()
    # Calculating difference between dates
    difference: datetime = date - today
    # Returning number of days
    return difference.days


# Test runs
print(get_days_from_today("2021-10-09"))
print(get_days_from_today("2024-05-01"))
print(get_days_from_today("2024-01-25"))
print(get_days_from_today("2025-04-12"))
print(get_days_from_today("2021.10.09"))
