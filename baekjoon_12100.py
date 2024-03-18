import copy

N = int(input())

MAP = list()

for _ in range(N):
     MAP.append(list(map(int, input().split())))


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


# 현재 맵에서 가장 큰 볼록의 값
def max_map(MAP):
     temp = 1
     for i in range(N):
          for j in range(N):
               if MAP[i][j] > temp:
                    temp = MAP[i][j]
     return temp


# 
def play(MAP, way):
     # 아래
     if way == 0: 
          # 블록을 체크하면서 결과를 다시씀
          for i in range(N):
               check = -1
               result = [0] * N
               count = 0
               for j in range(1, N+1): 
                    if MAP[-j][i] == 0:
                         continue
                    elif check == MAP[-j][i]:
                         result[count] = 2*check
                         count += 1
                         check = -1
                    else:
                         if check != -1:
                              result[count] = check
                              count += 1
                         check = MAP[-j][i]
               if check != -1:
                    result[count] = check
               result.sort(key=lambda x: x == 0)
               for j in range(N):
                    MAP[-j-1][i] = result[j]

     # 위
     elif way == 1:
          # 블록을 체크하면서 결과를 다시씀
          for i in range(N):
               check = -1
               result = [0] * N
               count = 0
               for j in range(N):
                    if MAP[j][i] == 0:
                         continue
                    elif check == MAP[j][i]:
                         result[count] = 2*check
                         count += 1
                         check = -1
                    else:
                         if check != -1:
                              result[count] = check
                              count += 1
                         check = MAP[j][i]
               if check != -1:
                    result[count] = check
               result.sort(key=lambda x: x == 0)
               for j in range(N):
                    MAP[j][i] = result[j]
     # 오른
     elif way == 2:
          # 블록을 체크하면서 결과를 다시씀
          for i in range(N):
               check = -1
               result = [0] * N
               count = 0
               for j in range(1, N+1):
                    if MAP[i][-j] == 0:
                         continue
                    elif check == MAP[i][-j]:
                         result[count] = 2*check
                         count += 1
                         check = -1
                    else:
                         if check != -1:
                              result[count] = check
                              count += 1
                         check = MAP[i][-j]
               if check != -1:
                    result[count] = check
               result.sort(key=lambda x: x == 0)
               for j in range(N):
                    MAP[i][-j-1] = result[j]

     # 왼
     elif way == 3:
          # 블록을 체크하면서 결과를 다시씀
          for i in range(N):
               check = -1
               result = [0] * N
               count = 0

               for j in range(N):
                    if MAP[i][j] == 0:
                         continue
                    elif check == 0:
                         check = -1
                    if check == MAP[i][j]:
                         result[count] = 2*check
                         count += 1
                         check = -1
                    else:
                         if check != -1:
                              result[count] = check
                              count += 1
                         check = MAP[i][j]
               if check != -1:
                    result[count] = check
               result.sort(key=lambda x: x == 0)
               for j in range(N):
                    MAP[i][j] = result[j]

     return MAP

def show_game(game):
     for i in range(N):
          print(*game[i], sep='\t')            

result = []
count_list = []
def dfs(game, way, count):
     count_list.append(count)
     # 현재 방향으로 합치기
     game2 = copy.deepcopy(game)
     game3 = play(game2, way)
     
     # print("---------------------------------------------", way)
     # show_game(game3)
     # print("-------------------------------------------------count : ", count+1)

     count += 1
     # 5번 이동했으면 종료
     if count == 5:
          result.append(max_map(game3))
          return

     # 아래, 위, 오른, 왼
     for i in range(4):
          dfs(game3, i, count)




for i in range(4):
     MAP2 = copy.deepcopy(MAP)
     dfs(MAP2, i, 0)
     # show_game(MAP)
# dfs(MAP, 3, 0)

print(max(result))
