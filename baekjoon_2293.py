n, k = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))

# 동전 오름차순 정렬
coins.sort()

# dp[i] = i원을 만드는 경우의 수
dp = [0] * (k+1)
dp[0] = 1

# 동전 종류를 하나씩 추가하면서 dp를 갱신
for coin in coins:
    # coin원부터 k원까지
    for i in range(coin, k+1):
        # i원을 만드는 경우의 수 += (i-coin)원을 만드는 경우의 수
        dp[i] += dp[i-coin]

print(dp[k])