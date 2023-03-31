"""
01타일
https://www.acmicpc.net/problem/1904
"""

n_in = int(input())

sols = [0 for _ in range(max(3, n_in + 1))]
sols[1] = 1
sols[2] = 2
for i in range(3, n_in + 1):
    sols[i] = (sols[i - 1] + sols[i - 2]) % 15746
    

print(sols[n_in])