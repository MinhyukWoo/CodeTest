def convert_to_ten_digit(string):
    sum_num = 0
    multiple = 1
    for char in string[::-1]:
        num = 0
        if char == "A":
            num = 10
        elif char == "B":
            num = 11
        elif char == "C":
            num = 12
        elif char == "D":
            num = 13
        elif char == "E":
            num = 14
        elif char == "F":
            num = 15
        else:
            num = int(char)
        sum_num += num * multiple
        multiple *= 16
    return sum_num


def solution(len_string, idx_max_num, numbers):
    max_rotation = len_string // 4
    dp = dict()
    for rotation in range(max_rotation):
        for idx in range(rotation, len(numbers), max_rotation):
            sub_numbers = (
                numbers[idx : idx + max_rotation]
                if idx + max_rotation <= len(numbers)
                else numbers[idx:] + numbers[: idx + max_rotation - len(numbers)]
            )
            dp[convert_to_ten_digit(sub_numbers)] = sub_numbers
    answers = list(sorted(dp.keys(), reverse=True))
    answer = answers[idx_max_num]
    return answer



if __name__ == "__main__":
    cnt_testcase = int(input())
    answers = []
    for _ in range(cnt_testcase):
        n, k = [int(char) for char in input().split(" ")]
        string = input()
        answers.append(solution(n, k-1, string))
        
    for idx, answer in enumerate(answers):
        print(f"#{idx+1} {answer}")
