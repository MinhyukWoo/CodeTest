"""
N-Queen
https://www.acmicpc.net/problem/9663

시간초과 때문에 pypy3로 제출

"""
n = int(input())


def f(nums, i):
    if i > len(nums):
        return 1
    else:
        out = 0
        mask = [True for _ in range(len(nums))]
        for j, num in enumerate(nums):
            if num != 0:
                mask[j] = False
                if j - (i - num) >= 0:
                    mask[j - (i - num)] = False
                if j + (i - num) < len(mask):
                    mask[j + (i - num)] = False
        for j, m in enumerate(mask):
            if m == True:
                nums[j] = i
                out += f(nums, i + 1)
                nums[j] = 0
        return out


out = f([0 for _ in range(n)], 1)
print(out)
