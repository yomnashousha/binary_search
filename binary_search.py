#!/bin/python3
'''

It's really easy to have off-by-1 errors in these problems.
Pay very close attention to your list indexes and your < vs <= operators.
'''


def find_smallest_positive(xs):
    '''
    Assume that xs is a list of numbers sorted from LOWEST to HIGHEST.
    Find the index of the smallest positive number.
    If no such index exists, return `None`.

    HINT:
    This is essentially the binary search algorithm from class,
    but you're always searching for 0.

    APPLICATION:
    This is a classic question for technical interviews.

    >>> find_smallest_positive([-3, -2, -1, 0, 1, 2, 3])
    4
    >>> find_smallest_positive([1, 2, 3])
    0
    >>> find_smallest_positive([-3, -2, -1]) is None
    True
    '''
    if len(xs) == 0:
        return None

    def go(left, right):
        if left == right:
            if xs[left] > 0:
                return left
            else:
                return None
        mid = (left + right) // 2
        if xs[mid] > 0:
            right = mid
        elif xs[mid] <= 0:
            left = mid + 1
        return go(left, right)
    return go(0, len(xs) - 1)


def count_repeats(xs, x):
    '''
    Assume that xs is a list of numbers sorted from HIGHEST to LOWEST,
    and that x is a number.
    Calculate the number of times that x occurs in xs.

    HINT:
    Use the following three step procedure:
        1) use binary search to find the lowest index with a value >= x
        2) use binary search to find the lowest index with a value < x
        3) return the difference between step 1 and 2
    I highly recommend creating stand-alone functions for steps 1 and 2,
    and write your own doctests for these functions.
    Then, once you're sure these functions work independently,
    completing step 3 will be easy.

    APPLICATION:
    This is a classic question for technical interviews.

    >>> count_repeats([5, 4, 3, 3, 3, 3, 3, 3, 3, 2, 1], 3)
    7
    >>> count_repeats([3, 2, 1], 4)
    0
    '''
    def lowest(left, right):
        if left < right:
            if xs[left] == x:
                return left
            mid = (left + right) // 2
            if xs[mid] > x:
                left = mid + 1
            if xs[mid] <= x:
                right = mid
        else:
            return left if xs[left] == x else -1
        return lowest(left, right)

    def highest(left, right):
        if left < right:
            if xs[right] == x:
                return right
            mid = (left + right) // 2
            if xs[mid] < x:
                right = mid - 1
            elif xs[mid] >= x and left != mid:
                left = mid + 1
            else:
                return left if xs[left] == x else -1
        else:
            return right if xs[right] == x else -1
        return highest(left, right)

    if xs:
        diff1 = lowest(0, len(xs) - 1)
        diff2 = highest(0, len(xs) - 1)
        diff = diff2 - diff1
        return diff + 1 if diff2 != -1 else 0
    else:
        return 0


def argmin(f, lo, hi, epsilon=1e-3):
    '''
    HINT:
    The basic algorithm is:
        1) The base case is when hi-lo < epsilon
        2) For each recursive call:
            a) select two points m1 and m2 that are between lo and hi
            b) one of the 4 points (lo,m1,m2,hi) must be the smallest;

    APPLICATION:

    WARNING:
    The doctests below are not intended to pass on your code,
    See the pytests for correct examples.

    >>> argmin(lambda x: (x-5)**2, -20, 20)
    5.000040370009773
    >>> argmin(lambda x: (x-5)**2, -20, 0)
    -0.00016935087808430278
    '''
    def go(lo, hi):
        m1 = lo + (hi - lo) / 3
        m2 = lo + (hi - lo) / 3 * 2

        if (hi - lo) < epsilon:
            return hi
        elif f(m2) > f(m1):
            return go(lo, m2)
        elif f(m1) > f(m2):
            return go(m1, hi)
    return go(lo, hi)


# the functions below are extra credit

def find_boundaries(f):
    '''
    Returns a tuple (lo,hi).
    This function is useful for initializing argmin.

    HINT:
    Begin with initial values lo=-1, hi=1.
    Let mid = (lo+hi)/2
    if f(lo) > f(mid):
        recurse with lo*=2
    elif f(hi) < f(mid):
        recurse with hi*=2
    else:
        you're done; return lo,hi
    '''
    lo = -1
    hi = 1
    while True:
        mid = (lo + hi) // 2
        if f(lo) < f(mid):
            lo *= 2
        elif f(hi) < f(mid):
            hi *= 2
        else:
            return (lo, hi)


def argmin_simple(f, epsilon=1e-3):
    '''
    you do not need to specify lo and hi.

    NOTE:
    There is nothing to implement for this function.
    If you implement the find_boundaries function correctly,
    then this function will work correctly too.
    '''
    lo, hi = find_boundaries(f)
    return argmin(f, lo, hi, epsilon)
