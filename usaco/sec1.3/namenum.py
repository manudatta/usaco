"""
ID: manu.da1
LANG: PYTHON3
TASK: namenum
"""
mappings = { '2': ('A','B','C')
            ,'5': ('J','K','L')
            ,'8': ('T','U','V')
            ,'3': ('D','E','F')
            ,'6': ('M','N','O')
            ,'9': ('W','X','Y')
            ,'4': ('G','H','I')
            ,'7': ('P','R','S') }



def get_serialno(fin):
    return str.rstrip(fin.readline())

def get_cownames(fdict):
    return map(str.rstrip,fdict.readlines())

def filter_names(names,serialno):
    tuples = [mappings[c] for c in serialno]
    L = len(tuples)
    matches = []
    for name in names:
        if len(name) == L:
            for c,t in zip(name,tuples):
                if c not in t:
                    break
            else:
                matches.append(name)
    return None if matches == [] else matches


def main():
    fin = open('namenum.in', 'r')
    fout = open('namenum.out', 'w')
    fdict = open('dict.txt', 'r')
    serialno = get_serialno(fin)
    names = get_cownames(fdict)
    names = filter_names(names,serialno)
    names = ["NONE"] if names is None else names
    for name in names:
        fout.write(name + '\n')
    fout.close()
    fin.close()
    fdict.close()
main()
