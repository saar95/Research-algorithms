import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def path_test(path):
    best_path = highest_value.get(path)
    if best_path != None:
        return best_path
    else:
        room = rooms[path]
        if room['door1']=='E': #exit
            door1 = int(room['money'])
        else:
            door1 = int(room['money']) + path_test(room['door1'])
        if room['door2']=='E': #exit
            door2 = int(room['money'])
        else:
            door2 = int(room['money']) + path_test(room['door2'])
        if door1<door2:
            best_path_cost = door2
        else:
            best_path_cost=door1
        highest_value[path] = best_path_cost
    return best_path_cost



# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

rooms = {}
highest_value = {}
n = int(input())
for i in range(n):
    N,money, door1, door2 = input().split()
    rooms[N] = {'money':money, 'door1':door1, 'door2':door2}
print(path_test('0'))