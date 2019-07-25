# STATEMENT: https://www.codingame.com/training/hard/turing-machine

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s, t, x = [int(i) for i in input().split()]
start = input()
n = int(input())

# q0 -> (symbol, shift, q1)
transition_func = {}

tape = [0]*t

for i in range(n):
    stateactions = input()
    state, actions = stateactions.split(":")
    action_list = actions.split(";")
    
    action_list = [act.split(" ") for act in action_list]
    transition_func[state] = action_list

    print(transition_func, file=sys.stderr)
    

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

state_reg = start
head_pos = x
n_actions = 0

while True:
    curr_symbol = tape[head_pos]
    write_symbol, move, state_reg = transition_func[state_reg][int(curr_symbol)]
    tape[head_pos] = write_symbol
    if move == 'R':
        head_pos += 1
    elif move == 'L':
        head_pos -= 1

    n_actions += 1

    if state_reg == 'HALT':
        break
    elif head_pos < 0:
        head_pos = -1
        break
    elif head_pos >= t:
        head_pos = t
        break

print(n_actions)
print(head_pos)
print(''.join(str(x) for x in tape))

