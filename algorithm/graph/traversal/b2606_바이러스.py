"""
바이러스
https://www.acmicpc.net/problem/2606
"""

a = {1: {1, 2, 3}}

len_computers = int(input())
len_edges = int(input())
edges = dict()
for _ in range(len_edges):
    a, b = input().split(" ")
    a, b = int(a), int(b)
    if edges.get(a, 0) == 0:
        edges[a] = set()
    if edges.get(b, 0) == 0:
        edges[b] = set()
    edges[a].add(b)
    edges[b].add(a)

visited_list = [False for _ in range(len_computers + 1)]
to_visit_list = [1]
out = 0
while len(to_visit_list) > 0:
    visit = to_visit_list.pop()
    if not visited_list[visit]:
        out += 1
        visited_list[visit] = True
        for next_visit in edges[visit]:
            to_visit_list.append(next_visit)
print(out - 1)