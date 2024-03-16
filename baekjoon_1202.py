import heapq
import sys
input = sys.stdin.readline


N, K = map(int, input().split())

jewel = []
K_list = []
K_heap = []

# 시간복잡도 O(N) -> 통과
for _ in range(N):
    M, V = map(int, input().split()) 
    jewel.append((M, V))

# 시간복잡도 O(K) -> 통과
for i in range(K):
    C = int(input())
    K_list.append(C)


# 시간복잡도 O(NlogN) -> 통과
jewel = sorted(jewel, key=lambda x:(x[0], -x[1]))

# 시간복잡도 O(KlogK) -> 통과
K_list = sorted(K_list, key=lambda x:x) # 힙을 사용해서 필요X



## 시간 초과 부분
"""
result = 0
for (M, V) in jewel:
    for i, C in enumerate(K_list):
        # print(K_list)
        if M <= C:
            result += V
            K_list.pop(i)
            break
"""

# 이진 탐색
"""
def binary_search(find, data):
    start = 0
    end = len(data) -1
    if end < 0:
        return -1
    if find > data[-1]:
        return -1

    while start<=end:
        mid = (start+end) // 2

        if data[mid] == find:
            return mid
        elif data[mid] > find:
            end = mid -1
        else:
            start = mid + 1

    return start
"""

# 가방에 넣을 수 있는 보석중 가장 가치가 큰것
result = 0
heap = []
for C in K_list:
    # if not jewel:
    #     break
    # 일단 가방크기보다 작은 보석들 heap에 담음
    while jewel and jewel[0][0] <= C:
        heapq.heappush(heap, -jewel[0][1])
        heapq.heappop(jewel)


    if heap:
        result -= heapq.heappop(heap)
    

print(result)
