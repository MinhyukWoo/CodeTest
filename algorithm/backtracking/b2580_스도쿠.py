"""
스도쿠
https://www.acmicpc.net/problem/2580
"""

board = [int(s) for _ in range(9) for s in input().split(" ")]


def getRowNum(i_board):
    return i_board // 9


def getColNum(i_board):
    return i_board % 9


def getGridNum(i_board):
    return 3 * (getRowNum(i_board) // 3) + (getColNum(i_board) // 3)


def getPromiseList(board, i_board):
    not_promise_list = set()
    row_num, col_num, grid_num = (
        getRowNum(i_board),
        getColNum(i_board),
        getGridNum(i_board),
    )
    for i in range(9 * 9):
        if (
            row_num == getRowNum(i)
            or col_num == getColNum(i)
            or grid_num == getGridNum(i)
        ):
            not_promise_list.add(board[i])
    return {i for i in range(1, 10)}.difference(not_promise_list)


def solve(board, i_board):
    if i_board == 9 * 9:
        return True
    elif board[i_board] == 0:
        promise_list = getPromiseList(board, i_board)
        if len(promise_list) == 0:
            return False
        else:
            for num in promise_list:
                board[i_board] = num
                is_solved = solve(board, i_board + 1)
                if is_solved:
                    return True
                else:
                    board[i_board] = 0
    else:
        return solve(board, i_board + 1)


solve(board, 0)
for i in range(9):
    for j in range(9):
        print(board[i * 9 + j], end=" ")
    print()
