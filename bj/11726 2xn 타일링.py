import sys
n=int(sys.stdin.readline().strip())
dp=[0 for i in range(n+4)]
dp[0]=0
dp[1]=1
dp[2]=2

for i in range(3,n+1):
    dp[i]=dp[i-1]+dp[i-2]

print(dp)
print(dp[n]%10007)