def solution():
    grid_size = int(input())
    student_wish_lists = dict()
    waitings = []
    for _ in range(grid_size**2):
        inputs = input().split(" ")
        waitings.append(inputs[0])
        student_wish_lists[inputs[0]] = set(inputs[1:])
    
    # 자리 앉히기: 괜히 sorted로 해결한 감이 있음
    seats = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
    for student in waitings:
        wish_seats = [
            [0, 0, idx // grid_size, idx % grid_size] for idx in range(grid_size ** 2)
        ]
        wish_list = student_wish_lists[student]
        for idx in range(grid_size):
            for jdx in range(grid_size):
                if seats[idx][jdx] in wish_list:
                    if idx > 0:
                        wish_seats[(idx-1) * grid_size + jdx][0] += 1
                    if idx < grid_size - 1:
                        wish_seats[(idx+1) * grid_size + jdx][0] += 1
                    if jdx > 0:
                        wish_seats[idx * grid_size + jdx-1][0] += 1
                    if jdx < grid_size - 1:
                        wish_seats[idx * grid_size + jdx+1][0] += 1
                if seats[idx][jdx] == 0:
                    if idx > 0:
                        wish_seats[(idx-1) * grid_size + jdx][1] += 1
                    if idx < grid_size - 1:
                        wish_seats[(idx+1) * grid_size + jdx][1] += 1
                    if jdx > 0:
                        wish_seats[idx * grid_size + jdx-1][1] += 1
                    if jdx < grid_size - 1:
                        wish_seats[idx * grid_size + jdx+1][1] += 1
                else:
                    wish_seats[idx * grid_size + jdx][0] = float("-inf")
        wish_seats.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
        for wish_seat in wish_seats:
            if wish_seat[0] >= 0:
                seats[wish_seat[2]][wish_seat[3]] = student
                break
            
    #만족도 조사
    answer = 0
    for idx in range(grid_size):
        for jdx in range(grid_size):
            student = seats[idx][jdx]
            cnt_friend = 0
            student_wish_list = student_wish_lists[student]
            if idx > 0 and seats[idx-1][jdx] in student_wish_list:
                cnt_friend += 1
            if idx < grid_size - 1 and seats[idx+1][jdx] in student_wish_list:
                cnt_friend += 1
            if jdx > 0 and seats[idx][jdx-1] in student_wish_list:
                cnt_friend += 1
            if jdx < grid_size - 1 and seats[idx][jdx+1] in student_wish_list:
                cnt_friend += 1
            if cnt_friend == 2:
                answer += 10
            elif cnt_friend == 3:
                answer += 100
            elif cnt_friend == 4:
                answer += 1000
            else:
                answer += cnt_friend
    print(answer)

if __name__ == "__main__":
    solution()
