def dfs(cur, depth, max_depth):
    global answer

    if depth == max_depth:
        return
    for idx in range(len(cur)):
        pass



T = int(input())
for tc in ['#' + str(t) for t in range(1, T + 1)]:
    arr, n = input().split()
    arr, n = [*arr], int(n)
    answer = 0
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
