import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.


# game loop
max1 = 0
max2 = 0
while True:

    for i in range(8):
        mountain_h = int(input())
        if mountain_h > max1:
            max1 = mountain_h
            max2 = i
    print(max2)
    max1 = 0
    max2 = 0