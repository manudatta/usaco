"""
ID: manu.da1
LANG: PYTHON3
TASK: dualpal
"""
import itertools
import string
import sys
from functools import partial 
BASE_RANGE = range(2, 11)
S_MAX = 10000


def get_integers(fin):
    return map(int, fin.readline().split())


def is_palindrome(s):
    return s == s[::-1]


def to_base(n, base):
    base_digits = string.digits + string.ascii_uppercase
    str_repr = []
    while n != 0:
        n, d = divmod(n, base)
        str_repr.append(base_digits[d])
    return ''.join(reversed(str_repr))


def take_count(pred, it, count):
    pcount = 0
    results = []
    def wrapper(x):
        nonlocal pcount
        count_match = False
        if pred(x):
            results.append(x)
            pcount += 1
            count_match = (count == pcount)
        return count_match
    count_satisfied = any((wrapper(i) for i in it))
    return results if count_satisfied else []


def is_palindrome_base(base, num):
    str_repr_square = to_base(num, base)
    return is_palindrome(str_repr_square)


def main():
    fin = open('dualpal.in', 'r')
    fout = open('dualpal.out', 'w')
    [N,S] = get_integers(fin)
    count = 0
    for num in range(S+1, sys.maxsize):
        pred = partial(is_palindrome_base, num=num)
        if take_count(pred, BASE_RANGE, 2) != []:
            fout.write(f'{num}\n')
            count += 1
        if count >= N:
            break
    fin.close()
    fout.close()


main()
