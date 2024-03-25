N = int(input())

posit = []

for i in range(N):
    x, y = map(int, input().split())
    posit.append((x, y))

# posit.sort(key=lambda x:x[0])


# 가장 높은 것의 index
Max_y = -100000
index = 0
for i, (nx, ny) in enumerate(posit):
    if ny > Max_y:
        Max_y = ny
        index = i


if index ==0:
    a = 0
    b = 1
elif index == 1:
    a = 0
    b = 2


result = 0

posit.append(posit[0])

for i in range(N):

    
    hap_1 = posit[i][0] * posit[i+1][1]
    hap_2 = posit[i+1][0] * posit[i][1]

    result += hap_1 - hap_2

print(round(abs(result)/2, 1))
