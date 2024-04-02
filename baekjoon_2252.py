from collections import deque

N, M = map(int, input().split())


parent = dict()


for i in range(1, N+1):
    parent[i] = []

num = [0 for i in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    parent[A].append(B)
    num[B] += 1


result = []


queue = deque()

for i in range(1, N+1):
    if num[i] == 0:
        queue.append(i)

while queue:
    pre = queue.popleft()
    result.append(pre)
    for i in parent[pre]:
        num[i] -= 1
        if num[i] == 0:
            queue.append(i)
    
print(*result)
