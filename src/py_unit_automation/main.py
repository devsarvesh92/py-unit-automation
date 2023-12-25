def factorial(number: int) -> int:
    """
    Get factorial of number using recursion

    Args:
        number (int): Number

    Returns:
        int: Factorial
    """
    if number == 0 or number == 1:
        return 1
    return number * factorial(number - 1)
