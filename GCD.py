def gcd_naive(a, b):
    """
    Naive algorithm that compares all possible
    common divisors and takes the maximum one.
    """
    gcd = 1
    max_gcd = min(max(a, b) // 2, min(a, b)) + 1

    for i in range(2, max_gcd):
        if a % i == 0 and b % i == 0:
            gcd = i

    return gcd


def gcd_div(a, b):
    """
    Alternative algorithm that finds that divisors for
    each number, and then finds the greatest common one.
    Slower than 'gcd_naive'
    """
    div_a = {i for i in range(2, a // 2 + 1) if a % i == 0}
    div_b = {i for i in range(2, b // 2 + 1) if b % i == 0}

    try:
        return max(div_a & div_b)
    except ValueError:
        return 1


def gcd_euclid(a, b):
    """
    Euclidean recursive algorithm that uses
    gcd(a, b) = gcd(b, a') = gcd(a', b) rule.
    a' = a % b.
    Consider using 'decimal.Decimal' for large numbers.
    """
    if b == 0:
        return a
    return gcd_euclid(b, a % b)


def gcd_bin(u, v):
    """
    Binary (Stein's) algorithm that computes GCD.
    Consider using 'decimal.Decimal' for large numbers.
    """
    if u == v:
        return u
    elif u == 0:
        return v
    elif v == 0:
        return u

    # 'k' is number of common factors of 2
    k = 0
    while u != v:
        flag_u = ((u % 2) == 0)
        flag_v = ((v % 2) == 0)

        # if both 'u' and 'v' are even
        if flag_u and flag_v:
            u = int(u / 2)
            v = int(v / 2)
            k += 1
        # 'u' is even and 'v' is odd
        elif flag_u and (not flag_v):
            u = int(u / 2)
        # 'u' is odd and 'v' is even
        elif (not flag_u) and flag_v:
            v = int(v / 2)
        # both are odd
        elif (not flag_u) and (not flag_v):
            if u >= v:
                u = (u - v) / 2
            else:
                u, v = (v - u) / 2, u

    return 2**k * v
