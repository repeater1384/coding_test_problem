from collections import deque


def bfs(sx=0, sy=0):
    # min_distance[y][x][0] => 벽 안부수고 x,y 까지 최소거리
    # min_distance[y][x][1] => 벽 부수고  x,y 까지 최소거리

    min_distance = [[[0, 0] for _ in range(M)] for _ in range(N)]
    queue = deque([(sx, sy, 0)])
    min_distance[sy][sx][0] = 1

    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while queue:
        cx, cy, crashed = queue.popleft()
        if cx == M - 1 and cy == N - 1:
            return min_distance[cy][cx][crashed]

        for dx, dy in d:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < M and 0 <= ny < N:

                # 이동할 곳이 벽이고, 아직 한번도 안부쉈으면
                if matrix[ny][nx] == '1' and not crashed:
                    min_distance[ny][nx][1] = min_distance[cy][cx][0] + 1
                    queue.append([nx, ny, 1])

                # 이동할 수 있고, 한번도 방문하지 않았으면 ( 같은 상태로 이미 방문했다면 최솟값이 아님 )
                elif matrix[ny][nx] == '0' and min_distance[ny][nx][crashed] == 0:
                    min_distance[ny][nx][crashed] = min_distance[cy][cx][crashed] + 1
                    queue.append([nx, ny, crashed])
    return -1


N, M = map(int, input().split())
matrix = [[*input()] for _ in range(N)]

answer = bfs()
print(answer)
