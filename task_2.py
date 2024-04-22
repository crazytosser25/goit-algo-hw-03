from random import sample

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    """Generates and returns a list of quantity unique random numbers between min (inclusive) and max (exclusive).
    Throws ValueError if the requested sample size is larger than the population or negative.
    
    Args:
        min (int): The minimum value for the range of random numbers to choose from (min - 1).
        max (int): The maximum value (exclusive) for the range of random numbers to choose from (max - 1000).
        quantity (int): The desired number of unique random numbers in the returned list (value between min and max).

    Returns:
        list:  A sorted list of quantity random numbers between min and max (inclusive). Returns empty list in case of wrong args.
    """
    # Forming empty list for results
    numbers = list()
    # Checking if min lower than max ant they are in range from 1 to 1000
    if 0 < min < max < 1000:
        # Checking if there are enough values for quantity
        if quantity < (max - min + 1):
            # Generating list of random numbers
            numbers = sample(range(min, (max+1)), quantity)
    
    # Sorting list and returning
    return sorted(numbers)


# Test run
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа (6 from 1-49):", lottery_numbers)

lottery_numbers = get_numbers_ticket(0, 50, 5)
print("Ваші лотерейні числа (5 from 0-50):", lottery_numbers)

lottery_numbers = get_numbers_ticket(1, 1001, 10)
print("Ваші лотерейні числа (10 from 1-1001):", lottery_numbers)

lottery_numbers = get_numbers_ticket(50, 50, 5)
print("Ваші лотерейні числа (5 from 50-50):", lottery_numbers)

lottery_numbers = get_numbers_ticket(1, 50, 0)
print("Ваші лотерейні числа (0 from 1-50):", lottery_numbers)

lottery_numbers = get_numbers_ticket(1, 50, 51)
print("Ваші лотерейні числа (51 from 1-50):", lottery_numbers)

lottery_numbers = get_numbers_ticket(10, 20, 15)
print("Ваші лотерейні числа (15 from 10-20):", lottery_numbers)

lottery_numbers = get_numbers_ticket(1, 10, 6)
print("Ваші лотерейні числа (6 from 1-10):", lottery_numbers)
