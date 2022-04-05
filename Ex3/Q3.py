import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

calculations  = []
date = 0
zero_list=[0]
one_list=[1]

n = int(input())
for i in range(n):
    j, d = [int(j) for j in input().split()]
    calculations.append((j, j + d))
    date = max(calculations[i][1], date )

timelist = zero_list * date
calculations.sort(key=lambda x: x[1])


def calc(calculations,timelist):
    result = 0
    for temp_calc_list in calculations:
        start=temp_calc_list[0]
        end = temp_calc_list[1]
        if 1 in timelist[start:end]:
            continue
        else:
            result += 1
            timelist[start:end] = one_list * (end - start)
    return result


print(calc(calculations,timelist))
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
