from random import randint
from decorateit.util import timer


def max_pair_prod_naive(lst):
    """
    Naive solution that compares products of all possible pairs.
    Works for both positive and negative values. Slowest.
    """
    if len(lst) == 0:
        return
    elif len(lst) == 1:
        return lst[0]

    n = len(lst)
    prod = 0
    for first in range(n):
        for second in range(first + 1, n):
            prod = max(prod, lst[first] * lst[second])
    return prod


@timer(times=100000)
def max_pair_prod_improved(lst):
    """
    Improved solution that looks for two maximum numbers
    and returns their product. Only for positive values.
    Fastest.
    """
    if len(lst) == 0:
        return
    elif len(lst) == 1:
        return lst[0]

    idx_max1 = lst.index(max(lst))
    max2 = max(lst[:idx_max1] + lst[idx_max1 + 1:])

    return lst[idx_max1] * max2


# TODO test 'max_pair_prod' using radix and counting sort
@timer(times=100000)
def max_pair_prod(lst):
    """
    Solution that sorts the given list and then
    takes the max product. Works for both positive
    and negative values. Optimal.
    """
    if len(lst) == 0:
        return
    elif len(lst) == 1:
        return lst[0]

    seq = sorted(lst[:])

    # if amount of negative numbers < 2
    if len([n for n in seq if n < 0]) < 2:
        return seq[-2] * seq[-1]
    # if amount of positive numbers < 2
    # including 0
    elif len([m for m in seq if m >= 0]) < 2:
        return seq[0] * seq[1]
    else:
        # separates the list into negative
        # and positive (with 0) portions
        pos = list(filter((0).__le__, seq))
        neg = list(filter((0).__gt__, seq))

        # takes max product out of two lists
        return max(
            pos[-2] * pos[-1],
            neg[0] * neg[1]
        )
