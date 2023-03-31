"""
1로 만들기
https://www.acmicpc.net/problem/1463
"""

n_in = int(input())

sols = [0 for _ in range(n_in + 1)]

sols[1] = 0

import sys

for i in range(2, n_in + 1):
    sol_div3 = sys.maxsize
    sol_div2 = sys.maxsize
    if i % 3 == 0:
        sol_div3 = 1 + sols[i // 3]
    if i % 2 == 0:
        sol_div2 = 1 + sols[i // 2]
    sol_minus1 = 1 + sols[i - 1]
    sols[i] = min(sol_minus1, sol_div2, sol_div3)

print(sols[n_in])