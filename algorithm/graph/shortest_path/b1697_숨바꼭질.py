"""
숨바꼭질
https://www.acmicpc.net/problem/1697
"""

n_in, k_in = (int(s) for s in input().split(" "))

from collections import deque


queue = deque()
queue.append(n_in)
visited = {n_in: 0}
while len(queue) > 0:
    pos = queue.pop()
    if pos == k_in:
        break
    if visited.get(pos + 1, 0) == 0:
        queue.appendleft(pos + 1)
        visited[pos + 1] = visited[pos] + 1
    if pos > 0 and visited.get(pos - 1, 0) == 0:
        queue.appendleft(pos - 1)
        visited[pos - 1] = visited[pos] + 1
    if pos < k_in and visited.get(pos * 2, 0) == 0:
        queue.appendleft(pos * 2)
        visited[pos * 2] = visited[pos] + 1

print(visited[k_in])
