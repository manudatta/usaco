"""
ID: manu.da1
LANG: PYTHON3
TASK: combo
"""
import itertools
from functools import reduce, lru_cache
from itertools import product 

def get_integer(fin):
    return int(fin.readline())

def get_integer_list(fin):
    return map(int, fin.readline().split())

def get_word_list(fin):
    return [s.strip() for s in fin.readlines()]


def get_next_two(start,end,n):
    count = 0
    while count < 2:
        count += 1
        if n == end:
            n = start
            yield n
        else:
            n += 1
            yield n

def get_prev_two(start,end,n):
    count = 0
    while count < 2:
        count += 1
        if n == start:
            n = end
            yield n 
        else:
            n -= 1
            yield n
def get_range(start,end,n):
    g1 = set(get_prev_two(start,end,n))
    g2 = set(get_next_two(start,end,n))
    g = g1.union(g2)
    g.add(n)
    return g

def main():
    fin = open('combo.in', 'r')
    fout = open('combo.out', 'w')
    count = get_integer(fin)
    comb1 = tuple(get_integer_list(fin))
    comb2 = tuple(get_integer_list(fin))
    overlap = 1
    for a,b in zip(comb1, comb2):
        r1 = get_range(1,count,a) 
        r2 = get_range(1,count,b)
        overlap = overlap*len(r1.intersection(r2))
    count = min(count,5)
    fout.write(str(2*count*count*count-overlap) + "\n")
    fin.close()
    fout.close()

main()
