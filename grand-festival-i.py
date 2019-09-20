# STATEMENT: https://www.codingame.com/training/medium/the-grand-festival---i

import sys
import math

# Total prize starting on day d with rest r.
def prize(d,r):
    if(d == N):
        return 0
    if(r == 0):
        return prize(d+1,R)
    
    if memo[d+1][R] == -1:
        prize_excluded = prize(d+1,R)
        memo[d+1][R] = prize_excluded
    else:
        prize_excluded = memo[d+1][R]
    if memo[d+1][r-1] == -1:
        prize_included = p[d] + prize(d+1,r-1)
        memo[d+1][r-1] = prize_included
    else:
        prize_included = memo[d+1][r-1]

    if(prize_excluded < prize_included):
        print(d, file=sys.stderr)

    return max(prize_excluded, prize_included)

if __name__ == "__main__":
    N = int(input())
    R = int(input())

    p = []

    for i in range(N):
        p.append(int(input()))

    memo = [[-1] * (R+1) for _ in range(N+1)]

    print(prize(0,R))