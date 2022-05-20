T = int(input())
for tc in ['#' + str(t) for t in range(1, T + 1)]:
    N = int(input())
    info = [[*map(int, input().split())] for _ in range(N)]  # x, y, s

    answer = [None] * N

    for i in range(N):
        status = [-1] * N
        max_influ = None
        for j in range(N):
            if i == j: continue
            xi, yi, si, xj, yj, sj = *info[i], *info[j]
            influ = sj / ((xj - xi) ** 2 + (yj - yi) ** 2)
            if si < influ:
                status[j] = influ
        if status.count(-1) == N:
            answer[i] = 'K'
        elif status.count(max(status)) >= 2:
            answer[i] = 'D'
        else:
            give_up = status.index(max(status)) + 1
            answer[i] = give_up
            for a in range(N):
                if answer[a] == i + 1:
                    answer[a] = give_up

    print(tc, *answer)
