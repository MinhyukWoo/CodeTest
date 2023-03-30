"""
N과 M (1)
https://www.acmicpc.net/problem/15649
"""

m, n = input().split()
m, n = int(m), int(n)

nums = list(range(1, m + 1))


def f(m, n, nums, outs: list):
    if len(outs) == n:
        print(str(" ").join(outs))
    else:
        for i, num in enumerate(nums):
            if num != 0:
                tmp = num
                nums[i] = 0
                outs.append(str(num))
                f(m, n, nums, outs)
                nums[i] = tmp
                outs.pop()


f(m, n, nums, [])
