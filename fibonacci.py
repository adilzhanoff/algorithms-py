from math import sqrt
from decorateit.util import optimise


@optimise
def fib_rec(n):
    """
    Naive algorithm that uses recursion. Сan be sped up using
    'optimise' decorator. Install 'decorateit' package and see
    help(optimise) for more info. Slowest.
    """
    if n < 2:
        return n
    return fib_rec(n - 2) + fib_rec(n - 1)


def fib_loop(n):
    """
    Improved algorithm that uses looping. Stores the sequence.
    """
    if n < 2:
        return n

    lst = [0, 1]
    for i in range(2, n + 1):
        lst.append(lst[-1] + lst[-2])

    return lst[-1]


def fib_count(n):
    """
    Similar to previous algorithm, but doesn't store the sequence.
    This is why works much faster.
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fib(n):
    """
    https://stackoverflow.com/users/1354439/piotr-dabkowski
    Piotr Dabkowski's algorithm that uses fast exponentiation
    to raise the matrix to the nth power.

    Probability of this algorithm being quicker than 'fib_count' for
    some value of 'n' is:
        • ~96-97 % for 24 <= n < 28
        • ~97-98 % for 28 <= n < 40
        • ~99+ % for n >= 40

    For the rest, probabilities are (obtained by making 1000000 iterations):
    n  |    %
    2  |  2.2435
    3  |  1.9226
    4  |  0.4094
    5  |  0.46
    6  |  0.5747
    7  |  0.5974
    8  |  0.4737
    9  |  0.5191
    10 |  0.626
    11 |  0.7069
    12 |  3.3426
    13 |  3.9917
    14 |  1.3156
    15 |  3.012
    16 |  0.8327
    17 |  1.315
    18 |  4.8963
    19 |  5.6301
    20 |  42.971
    21 |  38.048
    22 |  72.5131
    23 |  82.7531
    """
    v1, v2, v3 = 1, 1, 0
    for rec in bin(n)[3:]:
        calc = v2 * v2
        v1, v2, v3 = v1 * v1 + calc, (v1 + v3) * v2, calc + v3 * v3
        if rec == '1':
            v1, v2, v3 = v1 + v2, v1, v2
    return v2


def fib_closed(n):
    """
    Algorithm that uses closed-form expression to compute Nth
    Fibonacci number, but only works correctly until n = 71.

    After that, its result is always smaller than the correct answer.
    A deviation from it increases almost linearly, at n = 1000
    it's appr. -3.35 * 10**-12 %.

    Probability of this algorithm being quicker than 'fib_count' for
    some value of 'n' is ~99 % for 19 <= n < 72.
    For the rest, probabilities are (obtained by making 1000000 iterations):
    n  |     %
    2  |  0.3297
    3  |  0.3598
    4  |  0.3852
    5  |  0.4333
    6  |  0.4597
    7  |  0.4949
    8  |  0.5366
    9  |  0.5954
    10 |  0.6523
    11 |  0.9247
    12 |  1.5323
    13 |  13.2846
    14 |  12.2797
    15 |  46.5361
    16 |  69.2306
    17 |  95.923
    18 |  97.8232
    """
    val = sqrt(5)
    ratio = 1 / val
    return int(
        ratio * ((1 + val) / 2) ** n - ratio * ((1 - val) / 2) ** n
    )
