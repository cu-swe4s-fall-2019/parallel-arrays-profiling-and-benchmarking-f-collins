import math


"""Math functions for computing some statistical values
"""


def list_mean(L):
    """Computes the mean of a list of numbers

    Parameters:
        L: The list of input data.

    Returns:
        The mean of the numbers in L.
    """
    if L is None:
        return None

    for l in L:
        # NOTE: here we drop any non number from the list before computing the
        # mean. Because the list is consistent between the scope inside this
        # function and outside, modifying the list in this fashion stays.
        if not isinstance(l, (int, float)):
            print("Non number " + l + " in list, dropping.")
            L.remove(l)

    if len(L) == 0:
        return None

    return sum(L)/len(L)


def list_stdev(L):
    """Computes the standard deviation of a list of numbers

    Parameters:
        L: The list of input data.

    Returns:
        The standard deviation of the numbers in L.
    """
    if L is None:
        return None
    if len(L) == 0:
        return None

    stdev = 0

    # calling list_mean has the side effect of also removing any non numbers
    # from the list we're working with
    mean = list_mean(L)
    for l in L:
        stdev += (l - mean) ** 2

    return math.sqrt((1 / (len(L) - 1)) * stdev)
