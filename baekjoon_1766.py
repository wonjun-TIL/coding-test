N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

indegree = [0] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

import heapq

heap = []

for i in range(1, N+1):
    if indegree[i] == 0:
        heapq.heappush(heap, i)

while heap:
    node = heapq.heappop(heap)
    print(node, end=' ')
    for i in graph[node]:
        indegree[i] -= 1
        if indegree[i] == 0:
            heapq.heappush(heap, i)
