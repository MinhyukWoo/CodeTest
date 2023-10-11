import collections


def solution():
    answer = 0
    # 보드 초기화
    grid_size = int(input())
    board = []
    for _ in range(grid_size):
        board.append([int(char) for char in input().split(" ")])

    # 상어 초기화
    shark_size = 2
    shark_experience = 0
    sharkX, sharkY = (0, 0)
    for idx in range(grid_size):
        for jdx in range(grid_size):
            if board[idx][jdx] == 9:
                sharkX = idx
                sharkY = jdx
                break

    # 시뮬
    while True:
        # 먹이 찾기
        visited = [[False for _ in range(grid_size)] for _ in range(grid_size)]
        visited[sharkX][sharkY] = True
        queue = collections.deque()
        queue.append((0, sharkX, sharkY))
        food_position = []
        food_attribute = [float("inf"), grid_size, grid_size]
        while len(queue):
            cost, currX, currY = queue.popleft()
            next_positions = (
                (currX - 1, currY),
                (currX, currY - 1),
                (currX + 1, currY),
                (currX, currY + 1),
            )
            for nextX, nextY in next_positions:
                next_cost = cost + 1
                if (
                    nextX >= 0
                    and nextX < grid_size
                    and nextY >= 0
                    and nextY < grid_size
                    and not visited[nextX][nextY]
                    and board[nextX][nextY] <= shark_size
                ):
                    visited[nextX][nextY] = True
                    curr_food_cost, curr_foodX, curr_foodY = food_attribute
                    if (
                        board[nextX][nextY] < shark_size
                        and board[nextX][nextY] not in (0, 9)
                        and (
                            next_cost < curr_food_cost
                            or (next_cost == curr_food_cost and nextX < curr_foodX)
                            or (
                                next_cost == curr_food_cost
                                and nextX == curr_foodX
                                and nextY < curr_foodY
                            )
                        )
                    ):
                        food_position = [nextX, nextY]
                        food_attribute = [next_cost, nextX, nextY]
                    queue.append((next_cost, nextX, nextY))

        # 엄마 상어 호출?
        if len(food_position) == 0:
            break
        # 먹이로 이동 및 먹기
        board[sharkX][sharkY] = 0
        sharkX, sharkY = food_position
        shark_experience += 1
        if shark_experience == shark_size:
            shark_size += 1
            shark_experience = 0
        board[sharkX][sharkY] = 0
        answer += food_attribute[0]

    print(answer)


if __name__ == "__main__":
    solution()
