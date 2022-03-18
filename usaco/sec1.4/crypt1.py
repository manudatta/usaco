"""
ID: manu.da1
LANG: PYTHON3
TASK: crypt1
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

def row_mult(row,val):
    carry = 0
    results = []
    for i in row[::-1]:
        carry,val = divmod(carry+i*val,10)
        results.append(val)
    if carry:
        results.append(carry)
    return results.reverse()



@lru_cache(maxsize=128)
def is_good_pair(c, l):
    return (c[0] * c[1])//10 in l

@lru_cache(maxsize=128)
def is_good_pair_and_num(num, c, l):
    return c[0] * num in l

@lru_cache(maxsize=128)
def is_good_pair_pair(c1, c0, l):
    c00 = c0[0]
    c01 = c0[1]
    c10 = c1[0]
    c11 = c1[1]
    perms = ((c01,c10),(c00,c11))
    v = map(lambda c: is_good_pair(c,l), perms)
    if all(v):
        m = (c00*c11+c01*c10)
        if m % 10 in l:
            if m > 10:
                return m // 10 in l
            return True
    return False

@lru_cache(maxsize=128)
def is_good_pair_pair_num(num,c1, c0, l):
    c00,c01 = c0
    c10,c11 = c1
    top_row=num*100+c11*10+c01
    bottom_row=c10*10+c00
    m = top_row*bottom_row
    print("\n {}{}{}\n  {}{}\n_____\n{}".format(num,c1[1],c0[1],c1[0],c0[0],m))
    while m > 0:
        if m % 10 not in l:
            print("False")
            return False
        m = m // 10
    print("True")
    return True 

def print_dsol(c):
    print(" {}\n {}\n__".format(c[0],c[1]))

def print_tsol(c1,c0):
    print(" {}{}\n {}{}\n___".format(c1[1],c0[1],c1[0],c0[0]))

def ret_tsol(num,c1,c0):
    return "{}{}{}x{}{}".format(num,c1[1],c0[1],c1[0],c0[0])

def is_row_ok(num, digits):
    is_ok = True
    while is_ok and num > 0:
        if num % 10 not in digits:
            return False
        num = num // 10
    return is_ok


def brute_force(digits):
    x = 0
    y = 0
    z = 0
    len5 = 0
    strs = []
    for (a,b,c) in product(digits,repeat=3):
        for (d,e) in product(digits,repeat=2):
            #print(a,b,c,d,e)
            x = (100*a+10*b+c)
            y = (10*d+e)
            num = (100*a+10*b+c)*(10*d+e)
            num1 = x*e
            num2 = x*d
            num_str = "{}{}{}x{}{}={}={}+{}".format(a,b,c,d,e,num,num1,num2)
            is_ok = num1 < 1000 and num2 < 1000
            is_ok = is_ok and all(map(lambda x: is_row_ok(x, digits), [num,num1,num2])) 
            y += 1
            is_len_5 = len(str(num)) == 5
            is_len_4 = len(str(num)) == 4 
            if is_ok and is_len_4:
                strs.append(num_str)
            x += 1
    #print("x=",x,"y=",y, "len5=",len5, "z=",z,"strs=",len(strs))
    return strs


def main():
    fin = open('crypt1.in', 'r')
    fout = open('crypt1.out', 'w')
    count = get_integer(fin)
    digits = tuple(get_integer_list(fin))
    assert count == len(digits)
    sols = set(brute_force(digits))
    fout.write(str(len(sols)) + "\n")
    fin.close()
    fout.close()

main()
