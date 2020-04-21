"""
ID: manu.da1
LANG: PYTHON3
TASK: gift1
"""

def get_lines(fin):
    return [s.strip() for s in fin.readlines()]

def transfer(accounts,name,amount):
    new_value = []
    for n,val in accounts:
        if name == n:
            val += amount
        new_value.append((n,val))
    return new_value

def main():
    fin = open('gift1.in', 'r')
    fout = open('gift1.out', 'w')
    lines = get_lines(fin)
    friend_count = int(lines[0])
    friend_list = lines[1:friend_count+1]
    accounts = [(p,0) for p in friend_list]
    count = 0
    for i in range(friend_count):
        base_index = friend_count+i+1+count
        giver_name = lines[base_index]
        amount,beneficiary_count = list(map(int,lines[base_index+1].split()))
        count += 1
        per_person = amount if beneficiary_count==0 else amount//beneficiary_count
        beneficiaries = lines[base_index+2:base_index+2+beneficiary_count] 
        for beneficiary in beneficiaries:
            accounts = transfer(accounts, beneficiary, per_person)
        accounts = transfer(accounts, giver_name, -beneficiary_count*per_person)
        #print(giver_name,amount,beneficiary_count,beneficiaries)
        #print(accounts)
        count += beneficiary_count
    #print(friend_count,friend_list)
    for f,a in accounts:
        fout.write(f'{f} {a}\n')
    fout.close()

main()
