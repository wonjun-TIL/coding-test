
N = int(input())

# x = 

# for i in range(N):
#     x, y, z = map(int, input().split())


edges = []


# 메모리 N^2
"""
for i in range(N):
    for j in range(i+1, N):
        edges.append((i, j, min(abs(MAP[i][0] - MAP[j][0]), abs(MAP[i][1] - MAP[j][1]), abs(MAP[i][2] - MAP[j][2]))))
"""


# 공간복잡도 N
x_lists,y_lists,z_lists = [],[],[]
for i in range(N):
    x,y,z = map(int,input().split())
    x_lists.append((x,i))
    y_lists.append((y,i))
    z_lists.append((z,i))


x_lists.sort()
y_lists.sort()
z_lists.sort()

for i in range(1, N):
    x1, a1 = x_lists[i - 1]
    x2, b1 = x_lists[i]
    y1, a2 = y_lists[i - 1]
    y2, b2 = y_lists[i]
    z1, a3 = z_lists[i - 1]
    z2, b3 = z_lists[i]
    edges.append((a1, b1, abs(x1 - x2)))
    edges.append((a2, b2, abs(y1 - y2)))
    edges.append((a3, b3, abs(z1 - z2)))


edges.sort(key = lambda x : x[2])

# print(edges)

parent = [i for i in range(0, N+1)]
# print(result)



## 크루스칼 알고리즘

def find_parent(x):
    if parent[x] == x:
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

answer = 0
# 간선을 하나씩 확인하며
for edge in edges:
    a, b, cost = edge
    # 사이클 발생 안하는 경우에만 집합에 포함
    # print("----------------------")
    # print(*result)
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        # print(cost)
        answer += cost

print(answer)
