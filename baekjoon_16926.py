N, M, R = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]

for _ in range(R):
    for i in range(min(N, M)//2):
        temp = matrix[i][i]
        for j in range(i, M-i-1):
            matrix[i][j] = matrix[i][j+1]
        for j in range(i, N-i-1):
            matrix[j][M-i-1] = matrix[j+1][M-i-1]
        for j in range(M-i-1, i, -1):
            matrix[N-i-1][j] = matrix[N-i-1][j-1]
        for j in range(N-i-1, i, -1):
            matrix[j][i] = matrix[j-1][i]
        matrix[i+1][i] = temp

for row in matrix:
    print(*row)

    
 
