"""
연속합
https://www.acmicpc.net/problem/1912
"""

len_nums = int(input())
nums = [int(s) for s in input().split(' ')]

last_includes = [0 for _ in range(len_nums)]
sols = [0 for _ in range(len_nums)]

last_includes[0] = nums[0]
sols[0] = nums[0]

for i in range(1, len_nums):
    last_includes[i] = max(nums[i], last_includes[i-1] + nums[i])
    sols[i] = max(sols[i-1], last_includes[i])

print(sols[len_nums - 1])