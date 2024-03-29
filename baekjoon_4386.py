n = int(input())


Map = []
graph = []

for i in range(n):
    
    x, y = map(float, input().split())
    for star_num, sx, sy in Map:
        cost = ((sx-x)**2 + (sy-y)**2)**(1/2)
        graph.append((cost, star_num, i))

    Map.append((i, x, y))

graph.sort()

parent = [i for i in range(n+1)]

def find_parent(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find_parent(parent[x])
        return parent[x]
    
def union_parent(x,y):
    root_x = find_parent(x)
    root_y = find_parent(y)

    if root_x <= root_y:
        parent[root_y] = root_x
    else:
        parent[root_x] = root_y


result = 0
for cost, a, b in graph:
    if find_parent(a) == find_parent(b):
        continue
    else:
        union_parent(a, b)
        result+= cost

print(result)
