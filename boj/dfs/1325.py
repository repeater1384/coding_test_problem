# import sys
# input = sys.stdin.readline
# N, M = map(int, input().split())
#
#
# def dfs(start):
#     visit = set()
#     stack = [start]
#
#     depth = 0
#     while stack:
#         cur = stack.pop()
#         depth += 1
#         visit.add(cur)
#
#         for next in adj_list[cur]:
#             if not next in visit:
#                 stack.append(next)
#
#     return depth
#
#
# adj_list = [[] for _ in range(N + 1)]
# for _ in range(M):
#     a, b = map(int, input().split())
#     adj_list[b].append(a)
#
# result = []
# for start in range(1, N + 1):
#     result.append((start, dfs(start)))
#
# print(*[s for s, r in result if r == max(zip(*result))[1]])


import sys
from collections import deque


def bfs(start):
    visit = [False] * (N + 1)
    queue = deque([start])
    visit[start] = True
    depth = 1

    while queue:
        cur = queue.popleft()
        for next in adj_list[cur]:
            if not visit[next]:
                queue.append(next)
                visit[next] = True
                depth += 1
    return depth


input = sys.stdin.readline
N, M = map(int, input().split())

adj_list = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    adj_list[b].append(a)

answer = []
max_depth = -1
for start in range(1, N + 1):
    cur_depth = bfs(start)
    if max_depth < cur_depth:
        answer = [start]
        max_depth = cur_depth
    elif max_depth == cur_depth:
        answer.append(start)

print(*answer)
