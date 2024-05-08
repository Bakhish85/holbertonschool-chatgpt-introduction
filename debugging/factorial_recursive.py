#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given number.

    Function Description:
    This function calculates the factorial of a non-negative integer using recursion.
    The factorial of a non-negative integer n, denoted as n!, is the product of all
    positive integers less than or equal to n.

    Parameters:
    - n (int): The number for which factorial is to be calculated.

    Returns:
    int: The factorial of the input number n.
    """

    # Base case: if n is 0, factorial is 1
    if n == 0:
        return 1
    # Recursive case: calculate factorial recursively
    else:
        return n * factorial(n-1)

# Retrieve the command-line argument and calculate factorial
f = factorial(int(sys.argv[1]))
# Print the result
print(f)
