#exercise 1
def print_multiples(n, m):
    """
    >>> print_multiples("2", 4)
    Traceback (most recent call last):
    TypeError: the function expects two integers as input
    """

    if type(n) == str or type(m) == str:
        raise TypeError("the function expects two integers as input")
    if n < 0  or m < 0:
        raise ValueError("the second input must be non-negtaive")

    for num in range(1, m+1):
        mult = num * n
        print(mult, end=" ")

# print_multiples(3, 5)
# print_multiples('2', 5)
# print_multiples(3, -2)
