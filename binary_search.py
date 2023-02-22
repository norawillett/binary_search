#!/bin/python3
'''
JOKE: There are 2 hard problems in computer science: cache
invalidation, naming things, and off-by-1 errors.

It's really easy to have off-by-1 errors in these problems.
Py very close attention to your list indexes and your < vs <= operators.
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

    def go(xs, left, right):
        if left > right:
            return None
        mid = (left + right) // 2
        if xs[mid] > 0:
            if mid == 0 or xs[mid - 1] <= 0:
                return mid
            else:
                right = mid - 1
                return go(xs, left, right)
        else:
            left = mid + 1
            return go(xs, left, right)
    return go(xs, 0, len(xs) - 1)


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
    def last(xs, x, left, right):
        while left <= right:
            mid = (right + left) // 2
            if xs[mid] == x:
                if mid == len(xs) - 1 or xs[mid+1] != x:
                    return mid
                else:
                    left = mid + 1
            if xs[mid] < x:
                right = mid - 1
            else:
                left = mid + 1
        return -1
    b = last(xs, x, 0, len(xs) - 1)
    if b == -1:
        return 0

    def first(xs, x, left, right):
        while left <= right:
            mid = (right + left) // 2
            if xs[mid] == x:
                if mid == 0 or xs[mid-1] != x:
                    return mid
                else:
                    right = mid - 1
            if xs[mid] < x:
                right = mid - 1
            if xs[mid] > x:
                left = mid + 1
        return -1
    a = first(xs, x, 0, len(xs) - 1)
    if a == -1:
        return 0
    if x not in xs:
        return 0
    difference = (b-a) + 1
    return difference


def argmin(f, lo, hi, epsilon=1e-3):
    if (hi - lo) < epsilon:
        return (hi + lo) / 2
    m1 = lo + (hi - lo) / 2.5
    m2 = hi - (hi - lo) / 2.5

    if f(m1) < f(m2):
        return argmin(f, lo, m2, epsilon)
    else:
        return argmin(f, m1, hi, epsilon)
    '''
    >>> argmin(lambda x: (x-5)**2, -20, 20)
    5.000040370009773
    >>> argmin(lambda x: (x-5)**2, -20, 0)
    -0.00016935087808430278
    '''


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
