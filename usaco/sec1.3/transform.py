"""
ID: manu.da1
LANG: PYTHON3
TASK: transform
"""
from copy import deepcopy
def rotate_90(arr):
    dim = len(arr[0])
    out = deepcopy(arr)
    for i in range(dim):
        for j in range(dim):
            #print(j,dim-i-1)
            out[j][dim-i-1] = arr[i][j]
    return out

def rotate_180(arr):
    return rotate_90(rotate_90(arr))

def rotate_270(arr):
    return rotate_90(rotate_180(arr))

def reflect(arr,foo=None):
    arr = deepcopy(arr)
    if foo is None:
        return [list(reversed(row)) for row in arr]
    return foo([list(reversed(row)) for row in arr])



def get_integer(fin):
    return int(fin.readline())

def get_lines(fin):
    return [s.strip() for s in fin.readlines()]

def print_arr(arr):
    for row in arr:
        print(''.join(row))

def find_match(orig,final):
    rotations = [rotate_90,rotate_180,rotate_270]
    count = 1
    for foo in rotations:
        if(foo(orig)==final):
            return count
        if(reflect(orig,foo) == final):
            return 5 
        count+= 1
    if (final == reflect(orig)):
        return 4
    if orig == final:
        return 6
    return 7 

def main():
    fin = open('transform.in', 'r')
    fout = open('transform.out', 'w')
    line_count = get_integer(fin)
    inp = get_lines(fin)
    orig,final = [],[]
    for line in inp[0:line_count]:
        orig.append([c for c in line])
    for line in inp[line_count:]:
        final.append([c for c in line])
    cmd=str(find_match(orig,final))
    fout.write(cmd + '\n')
    fout.close()
    fin.close()

main()
