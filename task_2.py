from random import sample

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    """Generates and returns a list of quantity unique random numbers between min (inclusive) and max (exclusive).
    Throws ValueError if the requested sample size is larger than the population or negative.
    
    Args:
        min (int): The minimum value for the range of random numbers to choose from.
        max (int): The maximum value (exclusive) for the range of random numbers to choose from.
        quantity (int): The desired number of unique random numbers in the returned list.

    Returns:
        list:  A sorted list of quantity random numbers between min and max (inclusive).
    """
    try:
        # Generating list of random numbers
        numbers = sample(range(min, (max+1)), quantity)
    except ValueError:
        # Returning error if quantity is lagger than range 
        return 'ValueError: Sample larger than population or is negative!!!'
    # Sorting list and returning
    return sorted(numbers)


# Test run
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

lottery_numbers = get_numbers_ticket(1, 52, 6)
print("Ваші лотерейні числа:", lottery_numbers)

lottery_numbers = get_numbers_ticket(1, 36, 5)
print("Ваші лотерейні числа:", lottery_numbers)

lottery_numbers = get_numbers_ticket(1, 5, 6)
print("Ваші лотерейні числа:", lottery_numbers)
