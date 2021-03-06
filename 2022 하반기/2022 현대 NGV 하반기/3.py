"""
2022-07-29 횬다이 누가바 해몽

#3
문제)
N이 주어진다. (1<=N<=9)
N자리 숫자를 만들수 있다.
단, 숫자의 각 자리수 합이 9가 되면 안된다.

1000007로 나눈 나머지로 출력하라

sol)
관찰
- 1을 쓰면 8을 못쓴다. 2-7, 2-6 ... 9만 자유롭게 어디든 쓰일 수 있다.
- DP로 접근
- 이유 : 완전탐색으로는 100만자리 어려울 것 같아, DP로 접근

- 1-8, 2-7, 3-6, 4-5 의 관계를 정의 (A-B)
- dp(n,k) = n자리 자연수 중 정확히 k개의 선택지가 사용됨
ex)
dp(5,0) => 9 9 9 9 9
dp(5,1) => A 9 9 9 9
        => 9 A 9 A A
        => ...

dp(5,2) => ...

점화식
dp(1,0) = 1 -> 9
dp(1,1) = 1 -> A
dp(n,0) + dp(n,1)*2^1*4C1 + dp(n,2)*2^2*4C2 + dp(n,3)*2^3+4C3 + dp(n,4)*2^4+4C4
=> * A,B 선택하는 경우의 수 * 관계를 선택하는 조합의 수

dp(n,k)
1) 새로운 선택지 X
ㄱ) 9를 n
dp(n-1,k)
ㄴ) 선택지 중 1
dp(n-1,k)*k

2) 새로운 선택지 O
dp(n-1, k-1)    (k>0일 때 가능, 분기처리 필요)

다 더하면
dp(n, k) = dp(n-1,k) + dp(n-1,k-1) + dp(n-1,k)*k

"""

import sys
si = sys.stdin.readline
N = int(si())
MOD = 1000000007

dp =[[0 for _ in range(5)] for _ in range(N+1)]

dp[1][0] = 1
dp[0][1] = 1


for n in range(2, N+1):
    dp[n][0] =1
    for k in range(1,5):
        dp[n][k] = (dp[n-1][k-1]+dp[n-1][k]*(k+1))*MOD

ans = 0

ans = dp[n][0] + \
    dp[n][1] * 2 * 4 + \
    dp[n][2] * 4 * 12 + \
    dp[n][3] * 8 * 24 + \
    dp[n][4] * 16 * 24

print(ans)

