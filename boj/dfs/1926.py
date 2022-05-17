# # import sys
# #
# # sys.setrecursionlimit(10 ** 6)
# #
# # N, M = map(int, input().split())
# # matrix = [[*map(int, input().split())] for _ in range(N)]
# #
# #
# # def dfs(cx, cy,size=0):
# #     cur = 0
# #     matrix[cy][cx] = 0
# #     d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
# #
# #     for dx, dy in d:
# #         nx, ny = cx + dx, cy + dy
# #         if 0 <= nx < M and 0 <= ny < N:
# #             if matrix[ny][nx] == 1:
# #                 cur += dfs(nx, ny)
# #     return cur+size
# #
# #
# # count = 0
# # max_depth = -1
# # for y in range(N):
# #     for x in range(M):
# #         if matrix[y][x] == 1:
# #             count += 1
# #             max_depth = max(max_depth, dfs(x, y))
# #             for row in matrix:
# #                 print(row)
# #
# # print(count)
# # print(max_depth)
#
# import sys
#
# sys.setrecursionlimit(10 ** 6)
#
# N, M = map(int, input().split())
# matrix = [[*map(int, input().split())] for _ in range(N)]
#
#
# def dfs(cx, cy):
#     global depth
#     depth += 1
#
#     matrix[cy][cx] = 0
#     d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
#
#     for dx, dy in d:
#         nx, ny = cx + dx, cy + dy
#         if 0 <= nx < M and 0 <= ny < N:
#             if matrix[ny][nx] == 1:
#                 dfs(nx, ny)
#
#
# count = 0
# max_depth = 0
# for y in range(N):
#     for x in range(M):
#         if matrix[y][x] == 1:
#             count += 1
#             depth = 0
#             dfs(x, y)
#             max_depth = max(max_depth, depth)
#
# print(count)
# print(max_depth)


# import sys
#
# sys.setrecursionlimit(10 ** 6)
#
# N, M = map(int, input().split())
# matrix = [[*map(int, input().split())] for _ in range(N)]
#
#
# def dfs(cx, cy,size=0):
#     cur = 0
#     matrix[cy][cx] = 0
#     d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
#
#     for dx, dy in d:
#         nx, ny = cx + dx, cy + dy
#         if 0 <= nx < M and 0 <= ny < N:
#             if matrix[ny][nx] == 1:
#                 cur += dfs(nx, ny)
#     return cur+size
#
#
# count = 0
# max_depth = -1
# for y in range(N):
#     for x in range(M):
#         if matrix[y][x] == 1:
#             count += 1
#             max_depth = max(max_depth, dfs(x, y))
#             for row in matrix:
#                 print(row)
#
# print(count)
# print(max_depth)

N, M = map(int, input().split())
matrix = [[*map(int, input().split())] for _ in range(N)]


def dfs(sx, sy):
    depth = 0
    stack = [(sx, sy)]
    matrix[sy][sx] = 0

    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    while stack:
        cx, cy = stack.pop()
        depth += 1

        for dx, dy in d:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < M and 0 <= ny < N:
                if matrix[ny][nx] == 1:
                    stack.append((nx, ny))
                    matrix[ny][nx] = 0

    return depth


count = 0
max_depth = 0
for y in range(N):
    for x in range(M):
        if matrix[y][x] == 1:
            count += 1
            max_depth = max(max_depth, dfs(x, y))

print(count)
print(max_depth)
