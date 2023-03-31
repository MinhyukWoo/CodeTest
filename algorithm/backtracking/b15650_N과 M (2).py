"""
N과 M (2)
https://www.acmicpc.net/problem/15650
"""

m_in, n_in = input().split(" ")
m_in, n_in = int(m_in), int(n_in)


def func(nums, i_nums, max_len_nums, max_num):
    if i_nums == max_len_nums:
        for num in nums:
            print(num, end=" ")
        print()
    elif i_nums == 0:
        for num in range(1, max_num + 1):
            nums.append(num)
            func(nums, i_nums + 1, max_len_nums, max_num)
            nums.pop()
    else:
        for num in range(nums[i_nums - 1] + 1, max_num + 1):
            nums.append(num)
            func(nums, i_nums + 1, max_len_nums, max_num)
            nums.pop()


func([], 0, n_in, m_in)
