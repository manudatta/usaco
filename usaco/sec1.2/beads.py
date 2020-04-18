"""
ID: manu.da1
LANG: PYTHON3
TASK: beads
"""
#seq='wwwbbrwrbrbrrbrbrwrwwrbwrwrrb'
def get_word_list(fin):
    return [s.strip() for s in fin.readlines()]


def can_continue(start,last,nex):
    return True if nex == 'w' or last == 'w' else last == nex
    return False


def progress(seq,start,func,step=1):
    l = 1
    s = seq[start]
    L = len(seq)
    last = s
    match = []
    while l < L:
        index = (start+step*l)
        index = (start+step*l)%L
        n = seq[index]
        print(f"{start} {n} {index} {step}")
        if func(s,last,n):
            #print(s,last,n)
            l += 1 
        else:
            break
        match.append(n)
        if last == 'w' and n != 'w':
            last = n
    x = match.reverse() if step == -1 else None
    #print(f"{start} {l} {step} {match}")
    return l
def main():
    fin = open('beads.in', 'r')
    fout = open('beads.out', 'w')
    inp = get_word_list(fin)
    L = int(inp[0]) 
    seq = inp[1] 
    lens = []
    maximum = None
    for i in range(L):
        print(i,":",seq[0:i+1],":",seq[i+1:])
        f_l_i = progress(seq,i,can_continue)
        print(i,":",seq[0:i+1],":",seq[i+1:])
        b_l_i = progress(seq,i-1,can_continue,step=-1)
        lens.append((i,f_l_i,b_l_i))
        if maximum is None or maximum < f_l_i + b_l_i:
            maximum = f_l_i + b_l_i
    print(lens)
    maximum = L if maximum > L else maximum
    fout.write(str(maximum) + '\n')
    fout.close()
main()
