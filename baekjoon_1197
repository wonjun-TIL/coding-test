V, E = map(int, input().split())

graph = []

for _ in range(E):
    a, b, c = map(int, input().split())
    graph.append((a, b, c))

graph.sort(key=lambda x:x[2])

parent = [i for i in range(V+1)]

def find_parent(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find_parent(parent[x])
        return parent[x]

def union_parent(x, y):
    root_x = find_parent(x)
    root_y = find_parent(y)

    if root_x < root_y:
        parent[root_y] = root_x
    else:
        parent[root_x] = root_y

result = 0
for a, b, c in graph:
    if find_parent(a) == find_parent(b):
        continue
    else:
        union_parent(a, b)
        result += c
        


print(result)
