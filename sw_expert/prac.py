def combinations(arr, depth):
    for i in range(len(arr)):
        if depth == 1:
            yield arr[i]
        else:
            for next in combinations(arr[i + 1:], depth - 1):
                yield arr[i] + next

for comb in combinations([*map(str,range(5))], 2):
    a, b = comb
    print(a,b)