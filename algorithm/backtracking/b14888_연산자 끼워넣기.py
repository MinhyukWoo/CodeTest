"""
연산자 끼워넣기
https://www.acmicpc.net/problem/14888
"""

_ = input()
nums = [int(s) for s in input().split(" ")]
cnt_add, cnt_minus, cnt_mul, cnt_div = [int(s) for s in input().split(" ")]


import sys

min_out = sys.maxsize
max_out = -sys.maxsize
outs = [min_out, max_out]

def func(nums, pre_out, outs, i_nums, cnt_add, cnt_minus, cnt_mul, cnt_div):
    if i_nums == len(nums):
        outs[0] = min(pre_out, outs[0])
        outs[1] = max(pre_out, outs[1])
    elif i_nums == 0:
        func(nums, nums[0], outs, i_nums + 1, cnt_add, cnt_minus, cnt_mul, cnt_div)
    else:
        if cnt_add > 0:
            func(
                nums,
                pre_out + nums[i_nums],
                outs,
                i_nums + 1,
                cnt_add - 1,
                cnt_minus,
                cnt_mul,
                cnt_div,
            )
        if cnt_minus > 0:
            func(
                nums,
                pre_out - nums[i_nums],
                outs,
                i_nums + 1,
                cnt_add,
                cnt_minus - 1,
                cnt_mul,
                cnt_div,
            )
        if cnt_mul > 0:
            func(
                nums,
                pre_out * nums[i_nums],
                outs,
                i_nums + 1,
                cnt_add,
                cnt_minus,
                cnt_mul - 1,
                cnt_div,
            )
        if cnt_div > 0:
            func(
                nums,
                pre_out // nums[i_nums]
                if pre_out > 0
                else -1 * ((-1 * pre_out) // nums[i_nums]),
                outs,
                i_nums + 1,
                cnt_add,
                cnt_minus,
                cnt_mul,
                cnt_div - 1,
            )

func(nums, 0, outs, 0, cnt_add, cnt_minus, cnt_mul, cnt_div)

print(outs[1])
print(outs[0])