N, K, D = map(int, input().split())

student = []


for i in range(N):
    M, d = map(int, input().split())
    A = list(map(int, input().split()))
    student.append((M, d, A))


student.sort(key=lambda x: x[1])

index1 = 0
E = 0
A_list = [0]*(K+1)

for index2 in range(0, N):
    while student[index2][1] - student[index1][1] > D:
        for a in student[index1][2]:
            A_list[a-1] -= 1
        index1 += 1
    if student[index2][1] - student[index1][1] <= D:
        for a in student[index2][2]:
            A_list[a-1] += 1
        e1 = 0
        e2 = 0
        for a in A_list:
            if a >= 1:
                e1 += 1
            if a == index2-index1+1:
                e2 += 1
        E = max(E, (e1-e2)*(index2-index1+1))

print(E)
