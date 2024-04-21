from random import sample

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    try:
        numbers = sample(range(min, (max+1)), quantity)
    except ValueError:
        return 'ValueError: Sample larger than population or is negative!!!'
    return sorted(numbers)

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
