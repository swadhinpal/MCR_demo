
def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.
    more details added.
    """
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)
