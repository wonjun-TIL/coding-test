N = int(input())

MOD = 1000000000

dp = [[[0]*1024 for _ in range(10)] for _ in range(N+1)]

for i in range(1, 10):
    for j in range(10):
        dp[1][i][pow(2, i)] = 1

for i in range(2, N+1):
    for j in range(10):
        for k in range(1024):
            bit_mask = pow(2, j)  
            if j == 0:
                dp[i][j][k | bit_mask] += dp[i-1][j+1][k]
            elif j == 9:
                dp[i][j][k | bit_mask] += dp[i-1][j-1][k]
            else:
                dp[i][j][k | bit_mask] += dp[i-1][j-1][k]
                dp[i][j][k | bit_mask] += dp[i-1][j+1][k]


result = 0
for i in range(10):
    result += dp[N][i][1023]

print(result % MOD)
