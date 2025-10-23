#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given non-negative integer using recursion.

    Parameters:
        n (int): The number to compute the factorial of. 
                 Must be a non-negative integer.

    Returns:
        int: The factorial value of the input number 'n'.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Get the integer argument from the command line
f = factorial(int(sys.argv[1]))

# Print the computed factorial
print(f)

