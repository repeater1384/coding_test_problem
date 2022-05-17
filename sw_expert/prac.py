N = 7
for sy in range(N - 4):
    for sx in range(N - 1, 3, -1):
        for d in range(5):
            print(sy+d, sx-d,end=' ')
        print()