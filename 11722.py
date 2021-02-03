import sys
N = int(sys.stdin.readline())
subsequence = list(map(int, sys.stdin.readline().split()))
dp = [1] * N

for i in range(1, N):
    for j in range(i):
        print("//",i,"//")
        if subsequence[i] < subsequence[j]:
            print("i: %i" %i,"j: %i" %j)
            print("subsequence[%i]: " %i, subsequence[i] ,"subsequence[%i]: " %j, subsequence[j])
            print("j: ", j)
            print("dp[i]: ", dp[i], "dp[j]+1: ", dp[j] + 1)
            dp[i] = max(dp[i], dp[j] + 1)
            print(dp)
    print("-------")


print(max(dp))
