import sys

input = sys.stdin.readline
T = int(input())
for tc in ['#' + str(t) for t in range(1, T + 1)]:
    N = int(input())
    answer = 0
    for _ in range(N):
        x, y = map(int, input().split())
        dis = (x ** 2 + y ** 2) ** .5
        answer += max(10 - int(dis // 20), 0)

    print(tc, answer)

# 1206
# T = 10
# for tc in ['#' + str(t) for t in range(1, T + 1)]:
#     n = int(input())
#     arr = [*map(int, input().split())]
#     answer = 0
#
#     for i in range(2, n - 2):
#         cur = arr[i]
#         left, right = max(arr[i - 2:i]), max(arr[i + 1:i + 3])
#         if cur >= left and cur >= right:
#             answer += min(cur - left, cur - right)
#     print(tc, answer)
