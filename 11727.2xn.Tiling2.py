import sys

n = int(sys.stdin.readline())
# sx = 2 * n

dp = [0, 1, 3]

for i in range(3, 1000 + 1):
    dp.append((dp[i - 2] * 2) + (dp[i - 1]))

print(dp[n] % 10007)
