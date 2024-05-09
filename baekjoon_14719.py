
H, W = map(int, input().split())

blocks = list(map(int, input().split()))

answer = 0

for i in range(1, W-1):
    l = max(blocks[:i])
    r = max(blocks[i+1:])
    answer += max(0, min(l, r) - blocks[i])

print(answer)
