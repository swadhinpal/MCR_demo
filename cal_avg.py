
def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.
    more details added.
    """
    if not numbers:
        return 0
    if len(numbers) == 0 :
        return 0
    return sum(numbers) / len(numbers)
