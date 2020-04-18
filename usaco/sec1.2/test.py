"""
ID: manu.da1
LANG: PYTHON3
TASK: test
"""
def get_integer_list(fin):
    return map(int, fin.readline().split())

def main():
    fin = open('test.in', 'r')
    fout = open('test.out', 'w')
    sum_num = sum(get_integer_list(fin))
    fout.write(str(sum_num) + '\n')
    fout.close()
main()
