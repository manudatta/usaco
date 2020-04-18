"""
ID: manu.da1
LANG: PYTHON3
TASK: ride
"""
import itertools
from functools import reduce
def get_integer_list(fin):
    return map(int, fin.readline().split())
def get_word_list(fin):
    return [s.strip() for s in fin.readlines()]

def mod_s(s,const=47):
    f = lambda a,x : (ord(x)+1-ord('A'))*a
    return reduce(f,s,1) % const

def all_same(seq):
    l = list(itertools.dropwhile(lambda x: seq[0] == x,seq[1:]))
    return l == []

def main():
    fin = open('ride.in', 'r')
    fout = open('ride.out', 'w')
    mods = [mod_s(s) for s in get_word_list(fin)]
    cmd = "GO" if all_same(mods) else "STAY"
    #fout.write(str(all) + '\n')
    fout.write(cmd + '\n')
    fout.close()

main()
