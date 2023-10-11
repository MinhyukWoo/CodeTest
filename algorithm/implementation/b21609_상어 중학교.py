import collections


def find_max_block_group(grid_size, board):
    visited = [[False for _ in range(grid_size)] for _ in range(grid_size)]
    stack = collections.deque()
    max_group = []
    max_group_attrs = [float("-inf"), float("-inf"), float("inf"), float("inf")]
    for idx in range(grid_size):
        for jdx in range(grid_size):
            if visited[idx][jdx] or board[idx][jdx] <= 0:
                continue
            curr_group = []
            curr_group_attrs = [0, 0, idx, jdx]
            curr_group_type = board[idx][jdx]
            visited[idx][jdx] = True
            stack.append((idx, jdx))
            rainbows = []
            while len(stack):
                currX, currY = stack.pop()
                curr_group.append((currX, currY))
                next_positions = (
                    (currX - 1, currY),
                    (currX + 1, currY),
                    (currX, currY - 1),
                    (currX, currY + 1),
                )
                for nextX, nextY in next_positions:
                    if (
                        nextX >= 0
                        and nextX < grid_size
                        and nextY >= 0
                        and nextY < grid_size
                        and not visited[nextX][nextY]
                        and (
                            board[nextX][nextY] == curr_group_type
                            or board[nextX][nextY] == 0
                        )
                    ):
                        stack.append((nextX, nextY))
                        visited[nextX][nextY] = True
                        if board[nextX][nextY] == 0:
                            curr_group_attrs[1] += 1
                            rainbows.append((nextX, nextY))
            for currX, currY in rainbows:
                visited[currX][currY] = False
            curr_group_attrs[0] = len(curr_group)
            if (
                max_group_attrs[0] < curr_group_attrs[0]
                or (
                    max_group_attrs[0] == curr_group_attrs[0]
                    and max_group_attrs[1] < curr_group_attrs[1]
                )
                or (
                    max_group_attrs[0] == curr_group_attrs[0]
                    and max_group_attrs[1] == curr_group_attrs[1]
                    and max_group_attrs[2] < curr_group_attrs[2]
                )
                or (
                    max_group_attrs[0] == curr_group_attrs[0]
                    and max_group_attrs[1] == curr_group_attrs[1]
                    and max_group_attrs[2] == curr_group_attrs[2]
                    and max_group_attrs[3] < curr_group_attrs[3]
                )
            ):
                max_group = curr_group
                max_group_attrs = curr_group_attrs
    return max_group


def convert_to_score(board, group):
    for idx, jdx in group:
        board[idx][jdx] = -2
    return len(group) ** 2


def move_block_down(grid_size, board):
    for jdx in range(grid_size):
        idx_none = grid_size - 1 if board[-1][jdx] == -2 else grid_size - 2
        for idx in range(grid_size - 2, -1, -1):
            if board[idx][jdx] >= 0 and idx_none > idx:
                board[idx_none][jdx] = board[idx][jdx]
                board[idx][jdx] = -2
                next_idx_none = idx
                for kdx in range(idx_none - 1, -1, -1):
                    if board[kdx][jdx] == -2:
                        next_idx_none = kdx
                        break
                idx_none = next_idx_none
            elif board[idx][jdx] == -1:
                idx_none = idx
            if board[idx][jdx] != -2 and idx_none == idx:
                idx_none -= 1
            tmp = [board[i][jdx] for i in range(grid_size)]


def get_rotated_board(grid_size, board):
    new_board = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
    for idx in range(grid_size):
        for jdx in range(grid_size):
            new_board[idx][jdx] = board[jdx][grid_size - 1 - idx]
    return new_board


def solution():
    grid_size, max_type = [int(in_str) for in_str in input().split(" ")]
    board = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
    for idx in range(grid_size):
        inputs = input().split(" ")
        for jdx, in_str in enumerate(inputs):
            board[idx][jdx] = int(in_str)
    sum_score = 0

    while True:
        max_group = find_max_block_group(grid_size, board)
        if len(max_group) > 1:
            score = convert_to_score(board, max_group)
            sum_score += score
        else:
            break
        move_block_down(grid_size, board)
        rotated_board = get_rotated_board(grid_size, board)
        move_block_down(grid_size, rotated_board)
        board = rotated_board
    print(sum_score)


if __name__ == "__main__":
    solution()
