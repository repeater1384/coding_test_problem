T = input()
for tc in ['#' + str(t) for t in range(1, T + 1)]:
    n = int(input())
    arr = [*map(int, input().split())]
    answer = 0

    for i in range(1, n - 1):
        if arr[i] != min(arr[i - 1:i + 2]) and arr[i] != max(arr[i - 1:i + 2]):
            answer += 1
    print(tc, answer)