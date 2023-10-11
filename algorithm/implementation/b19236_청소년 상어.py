import copy
import collections


class TeenShark:
    def __init__(self):
        # 물고기 초기화
        self.board = []
        for _ in range(4):
            inputs = input().split(" ")
            row = []
            for idx in range(0, 8, 2):
                row.append([int(inputs[idx]), int(inputs[idx + 1]) - 1])
            self.board.append(row)

        self.fish_to_pos = dict()
        for idx in range(4):
            for jdx in range(4):
                self.fish_to_pos[self.board[idx][jdx][0]] = (idx, jdx)

        # 상어 초기화
        self.shark_num = -1
        self.answer = self.board[0][0][0]
        del self.fish_to_pos[self.board[0][0][0]]
        self.board[0][0][0] = self.shark_num
        self.sharkX, self.sharkY, self.shark_direction = (0, 0, self.board[0][0][1])

    def get_next_position(self, currX, currY, direction):
        if direction == 0:
            return (currX - 1, currY)
        elif direction == 1:
            return (currX - 1, currY - 1)
        elif direction == 2:
            return (currX, currY - 1)
        elif direction == 3:
            return (currX + 1, currY - 1)
        elif direction == 4:
            return (currX + 1, currY)
        elif direction == 5:
            return (currX + 1, currY + 1)
        elif direction == 6:
            return (currX, currY + 1)
        elif direction == 7:
            return (currX - 1, currY + 1)

    def move_fishes(self, board, fish_to_pos):
        for fish in range(1, 17):
            if fish in fish_to_pos:
                (currX, currY) = fish_to_pos[fish]
                next_direction = board[currX][currY][1]
                cnt_change_direction = 0
                while cnt_change_direction < 8:
                    nextX, nextY = self.get_next_position(currX, currY, next_direction)
                    if (
                        nextX >= 0
                        and nextX < 4
                        and nextY >= 0
                        and nextY < 4
                        and board[nextX][nextY][0] != self.shark_num
                    ):
                        tmp_fish_info = board[nextX][nextY]
                        board[nextX][nextY] = [fish, next_direction]
                        board[currX][currY] = tmp_fish_info
                        fish_to_pos[board[currX][currY][0]] = [currX, currY]
                        fish_to_pos[board[nextX][nextY][0]] = [nextX, nextY]
                        break
                    next_direction = (next_direction + 1) % 8
                    cnt_change_direction += 1

    def simulate(self):
        stack = collections.deque()
        stack.append(
            (
                self.sharkX,
                self.sharkY,
                self.shark_direction,
                self.board,
                self.fish_to_pos,
                self.answer,
            )
        )
        while len(stack):
            sharkX, sharkY, shark_direction, board, fish_to_pos, point = stack.pop()
            self.move_fishes(board, fish_to_pos)
            nextX, nextY = self.get_next_position(sharkX, sharkY, shark_direction)
            while nextX >= 0 and nextX < 4 and nextY >= 0 and nextY < 4:
                if board[nextX][nextY][0] > 0:
                    next_direction = board[nextX][nextY][1]
                    next_point = point + board[nextX][nextY][0]
                    next_fish_to_pos = copy.deepcopy(fish_to_pos)
                    del next_fish_to_pos[board[nextX][nextY][0]]
                    next_board = copy.deepcopy(board)
                    next_board[sharkX][sharkY][0] = 0
                    next_board[nextX][nextY][0] = self.shark_num
                    stack.append(
                        (
                            nextX,
                            nextY,
                            next_direction,
                            next_board,
                            next_fish_to_pos,
                            next_point,
                        )
                    )
                    if self.answer < next_point:
                        self.answer = next_point
                nextX, nextY = self.get_next_position(nextX, nextY, shark_direction)

        print(self.answer)


def solution():
    teen_shark = TeenShark()
    teen_shark.simulate()


if __name__ == "__main__":
    solution()
