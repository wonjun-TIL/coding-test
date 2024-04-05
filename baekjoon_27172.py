N = int(input())

x_list = list(map(int, input().split()))
x_lists= [0 for i in range(1000001)]

players = []
score = dict()

for i, x in enumerate(x_list):
    players.append((i, x))
    x_lists[x] = 1
    score[x] = 0

players.sort(key=lambda x : x[1])


for i in range(N):
    for j in range(players[i][1]*2, players[-1][1]+1,players[i][1]):
        if x_lists[j] == 1:
            score[players[i][1]] += 1
            score[j] -= 1

print(*score.values())
