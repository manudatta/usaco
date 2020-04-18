"""
ID: manu.da1
LANG: PYTHON3
TASK: milk2
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
    fin = open('milk2.in', 'r')
    fout = open('milk2.out', 'w')
    l = []
    count = get_integer(fin)
    print(count)
    for _ in range(count):
        [start,end] = get_integer_list(fin)
        print(start,end)
        l.append((start,'b'))
        l.append((end,'e'))
    l.sort()
    t,c = l[0]
    scount = 1
    longest_cont = 0
    longest_idle = 0
    start_idle,start_cont = 0,t
    for t,c in l[1:]:
        print(t,c,start_idle,start_cont)
        if c == 'b':
            if scount == 0:
                start_cont = t
                total_idle = t - start_idle
                if longest_idle < total_idle:
                    longest_idle = total_idle
            scount += 1
        else:
            scount -= 1
            if scount == 0:
                start_idle = t
                total_cont = t - start_cont
                if total_cont > longest_cont:
                    longest_cont = total_cont
        print(t,c,longest_cont,longest_idle)

    print(l)
    fout.write(f"{longest_cont} {longest_idle}" + '\n')
    # fout.write(cmd + '\n')
    fin.close()
    fout.close()

main()
