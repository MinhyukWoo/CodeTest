def get_next_ball_info(grid_size, board, warps, currX, currY, curr_direction):
    # 0 is UP, 1 is RIGHT, 2 is DOWN 3, is LEFT
    diffs = (
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1),
    )
    score = 0
    is_move_ended = False
    answer = []
    while not is_move_ended:
        nextX, nextY = (
            currX + diffs[curr_direction][0],
            currY + diffs[curr_direction][1],
        )
        if nextX < 0 or nextX >= grid_size or nextY < 0 or nextY >= grid_size:
            score += 1
            curr_direction = (curr_direction + 2) % 4
        elif board[nextX][nextY] == 0 or board[nextX][nextY] == -1:
            answer = [nextX, nextY, curr_direction, score]
            is_move_ended = True
            break
        elif board[nextX][nextY] in (1, 2, 3, 4, 5):
            score += 1
            block_type = board[nextX][nextY]
            if block_type == 5 or curr_direction in (block_type - 1, block_type % 4):
                curr_direction = (curr_direction + 2) % 4
            elif curr_direction == ((block_type + 1) % 4):
                curr_direction = (curr_direction - 1) % 4
            elif curr_direction == ((block_type + 2) % 4):
                curr_direction = (curr_direction + 1) % 4
        elif board[nextX][nextY] in (6, 7, 8, 9, 10):
            nextX, nextY = warps[(nextX, nextY)]
        currX, currY = (nextX, nextY)
    return answer


def simulate(grid_size, board, warps, startX, startY, direction):
    sum_score = 0
    is_game_over = False
    currX, currY, curr_direction = startX, startY, direction
    while not is_game_over:
        nextX, nextY, next_direction, score = get_next_ball_info(
            grid_size, board, warps, currX, currY, curr_direction
        )
        sum_score += score
        if (nextX == startX and nextY == startY) or board[nextX][nextY] == -1:
            is_game_over = True
            break
        currX, currY, curr_direction = nextX, nextY, next_direction

    return sum_score


def solution(grid_size, board):
    high_score = 0
    wormholes = dict()
    for idx in range(grid_size):
        for jdx in range(grid_size):
            if board[idx][jdx] in (6, 7, 8, 9, 10):
                type_wormhole = board[idx][jdx]
                if type_wormhole not in wormholes:
                    wormholes[type_wormhole] = []
                wormholes[type_wormhole].append((idx, jdx))
    warps = dict()
    for values in wormholes.values():
        warps[values[0]] = values[1]
        warps[values[1]] = values[0]

    for startX in range(grid_size):
        for startY in range(grid_size):
            if board[startX][startY] == 0:
                for direction in range(4):
                    score = simulate(grid_size, board, warps, startX, startY, direction)
                    high_score = score if score > high_score else high_score
    return high_score


if __name__ == "__main__":
    cnt_testcase = int(input())
    answers = []
    for _ in range(cnt_testcase):
        grid_size = int(input())
        board = []
        for _ in range(grid_size):
            row = [int(char) for char in input().strip().split(" ")]
            board.append(row)
        answers.append(solution(grid_size, board))
    for idx, answer in enumerate(answers):
        print(f"#{idx+1} {answer}")
