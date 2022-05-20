T = int(input())


def dfs(cx, cy, cur_status=''):
    if len(cur_status) == 7:
        result.add(cur_status)
        return

    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for dx, dy in d:
        nx, ny = cx + dx, cy + dy
        if 0 <= nx < 4 and 0 <= ny < 4:
            dfs(nx, ny, cur_status + matrix[ny][nx])


for tc in ['#' + str(t) for t in range(1, T + 1)]:
    matrix = [[*input().split()] for _ in range(4)]
    result = set()
    for sy in range(4):
        for sx in range(4):
            dfs(sx, sy)

    print(tc, len(result))
