#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculates the factorial of a given non-negative integer using recursion.

    Parameters:
    n (int): A non-negative integer for which the factorial is to be computed.

    Returns:
    int: The factorial of the input number 'n'.
         If n == 0, it returns 1 as the factorial of 0 is 1.
         Otherwise, it recursively calculates the factorial by multiplying n with factorial(n-1).
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Read an integer from the command-line argument, compute its factorial, and print it.
f = factorial(int(sys.argv[1]))
print(f)