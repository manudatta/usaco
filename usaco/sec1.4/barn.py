"""
ID: manu.da1
LANG: PYTHON3
TASK: barn1
"""
def get_integer_list(fin):
    return map(int, fin.readline().split())

def get_integer(fin):
    return int(fin.readline())

def main():
    fin = open('barn1.in', 'r')
    fout = open('barn1.out', 'w')
    [m,s,c] = get_integer_list(fin)
    occupied_barns = [get_integer(fin) for _ in range(c)]
    occupied_barns.sort()
    i = 0
    gaps = []
    start, end = occupied_barns[0], occupied_barns[-1]
    cells = end - start + 1
    if m != 1:
        i = 1
        while start < end:
            gap = 0
            while start < end and start == occupied_barns[i]-1:
                start += 1
                i += 1
            if start != end:
                gap = occupied_barns[i] - start - 1
                start = occupied_barns[i]
                i += 1
                gaps.append(gap)
    gaps.sort()
    print(gaps)
    cells = cells - sum(gaps[-(m-1):])
    fout.write(f"{cells}\n")
    fout.close()


main()
