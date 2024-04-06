
N, M = map(int, input().split())

city = [list(map(int, input().split())) for _ in range(N)]

chicken = []
house = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))

from itertools import combinations

result = 2000

for comb in combinations(chicken, M):
    temp = 0
    for hx, hy in house:
        min_distance = 2000
        for cx, cy in comb:
            min_distance = min(min_distance, abs(hx-cx) + abs(hy-cy))
        temp += min_distance

    result = min(result, temp)

print(result)
