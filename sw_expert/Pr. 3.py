T = 10


def dfs():
    sx, sy, ex, ey = *start, *end
    visited = [[False] * 16 for _ in range(16)]

    stack = [(sx, sy)]
    visited[sy][sx] = True

    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    while stack:
        cx, cy = stack.pop()

        if cx == ex and cy == ey:
            return 1

        for dx, dy in d:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < 16 and 0 <= ny < 16:
                if not visited[ny][nx]:
                    if matrix[ny][nx] != 1:
                        stack.append((nx, ny))
                        visited[ny][nx] = True

    return 0


for tc in ['#' + str(t) for t in range(1, T + 1)]:
    input()
    matrix = [[*map(int, input())] for _ in range(16)]

    for y in range(16):
        for x in range(16):
            if matrix[y][x] == 2:
                start = x, y
            if matrix[y][x] == 3:
                end = x, y
    print(tc, dfs())
