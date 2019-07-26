# STATEMENT: https://www.codingame.com/training/medium/elementary-cellular-automaton

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

r = int(input())
n = int(input())
start_pattern = input()
rule = bin(r).replace("0b","").zfill(8)
transf_rule = {}

for i in range(8):
    transf_rule[str(bin(7-i)).replace("0b","").zfill(3)] = rule[i]

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(start_pattern)

curr_pattern = start_pattern.replace("@","1").replace(".","0")
pat_len = len(curr_pattern)
for i in range(n-1):
    new_pattern = []
    for j in range(pat_len):
        neighbours = curr_pattern[j-1] + curr_pattern[j] + curr_pattern[(j+1) % pat_len]
        new_pattern.append(transf_rule[neighbours])
    curr_pattern = ''.join(new_pattern)
    print(curr_pattern.replace("1","@").replace("0","."))
