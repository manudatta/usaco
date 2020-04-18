"""
ID: manu.da1
LANG: PYTHON3
TASK: milk
"""
import itertools
from functools import reduce

def get_integer(fin):
    return int(fin.readline())

def get_integer_list(fin):
    return map(int, fin.readline().split())

def get_word_list(fin):
    return [s.strip() for s in fin.readlines()]


def main():
    fin = open('milk.in', 'r')
    fout = open('milk.out', 'w')
    [left,m] = get_integer_list(fin)
    prices = []
    for _ in range(m):
        price = tuple(get_integer_list(fin))
        prices.append(price)
    prices.sort()
    min_price = 0
    for p,v in prices:
        if left >= v:
            min_price += v*p
            left = left-v
        else:
            min_price += left*p
            break
    fout.write(f"{min_price}\n")
    fin.close()
    fout.close()

main()
