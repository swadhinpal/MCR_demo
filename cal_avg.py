
def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.
    """
    if not numbers:
        return 0
    print ("Calculating average for numbers:", numbers);
    return sum(numbers) / len(numbers)
