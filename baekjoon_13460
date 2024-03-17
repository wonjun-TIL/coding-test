import copy
from collections import deque

N, M = map(int, input().split())

MAP = list()

for _ in range(N):
    row = list(input())
    MAP.append(row)

di = [0, 1, 2, 3] # 위 오른 아래 왼


# 색깔공 위치 찾기
def find_colorball():

    result =[0, 0, 0]

    for i in range(N):
        for j in range(M):
            if MAP[i][j] == 'B':
                result[0] = (i, j)
            if MAP[i][j] == 'R':
                result[1] = (i, j)
            if MAP[i][j] == 'O':
                result[2] = (i, j)
    return result


# 비어있는 칸인지 확인
def is_bin(row, col, temp_map):
    if temp_map[row][col] =='.':
        return True
    else:
        return False
    


# 파랑먼저 빨강먼저?
def which_first(way, pBlue, pRed):
    if way == 0: # 위로
        if pBlue[0] < pRed[0]:
            return 2
        elif pBlue[0] > pRed[0]:
            return 1
        else:
            return 0
    elif way == 1: # 오른쪽
        if pBlue[1] < pRed[1]:
            return 1
        elif pBlue[1] > pRed[1]:
            return 2
        else:
            return 0
    elif way == 2: # 아래
        if pBlue[0] < pRed[0]:
            return 1
        elif pBlue[0] > pRed[0]:
            return 2
        else:
            return 0
    elif way == 3: # 왼
        if pBlue[1] < pRed[1]:
            return 2
        elif pBlue[1] > pRed[1]:
            return 1
        else:
            return 0



dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


# 하나의 방향으로 움직임
def move_way(node, temp_map, pBlue, pRed, pGoal):
    
    # 1이면 빨강이, 2면 파랑이 먼저움직임. 0이면 상관X
    first_move = which_first(node, pBlue, pRed)
    # print("moveway", node)
    gx, gy = pGoal
    flag = True
    result = 0

    # print("######################3PBlue", pBlue)
    # print("########################pRed", pRed)



    if first_move == 2 or first_move == 0:
        pos = pBlue
        pos2 = pRed
        flag = True
    else:
        pos = pRed
        pos2 = pBlue
        flag = False


    x = pos[0]
    y = pos[1]

    # print('flag', flag)
    while True:
        new_x = x + dy[node]
        new_y = y + dx[node]

        if new_x == gx and new_y == gy:
            if flag == True:
                return 2
            else:
                result = 1
                temp_map[x][y] = '.'
                pos = (x, y) 
                break

        if is_bin(new_x, new_y, temp_map):
            if flag:
                temp_map[new_x][new_y] = 'B'
            else:
                temp_map[new_x][new_y] = 'R'

            temp_map[x][y] = '.'
            
            x = new_x
            y = new_y

        else:
            pos = (x, y)
            break
    


    x = pos2[0]
    y = pos2[1]
    while True:
        new_x = x + dy[node]
        new_y = y + dx[node]

        # print('x', x)
        # print('y', y)
        # print("new_x", new_x)
        # print("new_y", new_y)
        # print('node', node)
        if new_x == gx and new_y == gy:
            if flag == True:
                # print("여기 들어왔음1")
                return 1
            else:
                # print("여기 들어왔음2")
                return 2

        if is_bin(new_x, new_y, temp_map):
            if flag:
                temp_map[new_x][new_y] = 'R'
            else:
                temp_map[new_x][new_y] = 'B'

            temp_map[x][y] = '.'
            
            x = new_x
            y = new_y

        else:
            # print('여기들어왔음3')
            # print(x, y)
            # print(gx, gy)
            pos2 = (x, y)
            break
    
    if result == 1:
        return 1
    elif flag == True:
        return (pos, pos2)
    else:
        return (pos2, pos)
    



        
    
        


# 모든 경로 움직임
def move(node_list, pBlue, pRed, pGoal):
    temp_map = copy.deepcopy(MAP)

    for node in node_list:
        result = move_way(node, temp_map, pBlue, pRed, pGoal)
        if result == 1: ## 성공
            return 1
        if result == 2: ## 파란공 들어감
            return 2
        
        temp_map[pBlue[0]][pBlue[1]] = '.'
        temp_map[pRed[0]][pRed[1]] = '.'

        pBlue, pRed = result
        
        temp_map[pBlue[0]][pBlue[1]] = 'B'
        temp_map[pRed[0]][pRed[1]] = 'R'


        # for row in temp_map:
        #     print(*row)

        # print("------------------------")

        
    return -1


graph = {
    0 : [1, 2, 3], 
    1 : [0, 2, 3],
    2 : [0, 1, 3], 
    3 : [0, 1, 2]
}


def bfs(graph):
    queue = deque([[0], [1], [2], [3]])

    pList = find_colorball()


    while queue:
        # print('queue', queue)
        node_list = queue.popleft() # 큐에서 노드 하나 꺼냄 # 노드는 경로 리스트
        # print('node_list', node_list) # 노드 출력해보기

        result = move(node_list, pList[0],pList[1],pList[2]) # 한번 이동해보기
        
        if result == 1: # 성공시 끝
            return len(node_list)
        elif result == 2: # 파란공 들어감 이번턴 무시
            continue

        if len(node_list) > 10:
            return -1
        
        node = node_list[-1]
        # print('node', node)
        for neighbor in graph[node]: # 현재 노드의 이웃 노드들
            new_node = copy.deepcopy(node_list)
            new_node.append(neighbor)
            # print('new_node', new_node)
            queue.append(new_node) # 큐에 추가



print(bfs(graph))


