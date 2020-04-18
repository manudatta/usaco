"""
ID: manu.da1
LANG: PYTHON3
TASK: friday
"""
thirty_day_months = [3,5,8,10]
#seq='wwwbbrwrbrbrrbrbrwrwwrbwrwrrb'
def get_word_list(fin):
    return [s.strip() for s in fin.readlines()]


def count_thirteenth(start_year,year_count):
    print(year_count)
    start_day_year = 1 # Monday 1900
    count = [0 for i in range(7)]
    for i in range(year_count):
        curr_year = i+start_year
        print(curr_year)
        leap = is_leap(curr_year)
        start_day_month = start_day_year
        days_in_month = 31 
        for j in range(12):
            count_index = (start_day_month + 12)%7
            count[count_index] += 1
            print(f"{j}: {start_day_month} {count_index} {count}")
            if j == 1: # feb
                days_in_month = 29 if leap else 28
            elif j in thirty_day_months:
                days_in_month = 30
            else:
                days_in_month = 31
            print(f"{days_in_month}")
            start_day_month = (start_day_month+days_in_month%7) % 7
        start_day_year += 2 if leap else 1
        start_day_year = start_day_year % 7
        start_day_month = start_day_year
        print(f"{start_day_year} {start_day_month}")
    return count[-1:]+count[0:-1]

def is_leap(year):
    is_divisble_by_4 = (year % 4) == 0
    is_divisble_by_100 = (year % 100) == 0
    is_divisble_by_400 = (year % 400) == 0
    #print(year,is_divisble_by_4,is_divisble_by_100,is_divisble_by_400)
    if is_divisble_by_4:
        if is_divisble_by_400:
            return True
        elif is_divisble_by_100:
            return False
        return True
    return False


def main():
    fin = open('friday.in', 'r')
    fout = open('friday.out', 'w')
    start_year = 1900
    year_count = int(get_word_list(fin)[0])
    freq = count_thirteenth(start_year, year_count)
    freq_str = ' '.join(map(str,freq))
    fout.write(freq_str + '\n')
    fout.close()
    fin.close()

main()
