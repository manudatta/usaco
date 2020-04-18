"""
ID: manu.da1
LANG: PYTHON3
TASK: palsquare
"""
import itertools
from functools import reduce
import string
LIMIT = 300

def get_integer(fin):
    return int(fin.readline())

def is_palindrome(s):
    return s == s[::-1]

def to_base(n,base):
    base_digits = string.digits + string.ascii_uppercase
    str_repr = [] 
    while n != 0:
        n,d = divmod(n,base)
        str_repr.append(base_digits[d])
        #print(n,d,str_repr)
    return ''.join(reversed(str_repr))

def main():
    fin = open('palsquare.in', 'r')
    fout = open('palsquare.out', 'w')
    base = get_integer(fin)
    N = 300
    for i in range(1,N+1):
        str_repr_square = to_base(i*i,base)
        if is_palindrome(str_repr_square):
            str_repr = to_base(i,base)
            s = f"{str_repr} {str_repr_square}"
            fout.write(s + '\n')
    fin.close()
    fout.close()

main()
