N, M, Q = map(int, input().split())

S = [[] for _ in range(N)]
P = [N] * M

for _ in range(Q):
    flag, *arg = map(int, input().split())
    if flag == 1:
        n = arg[0] - 1
        ans = sum(P[i] for i in S[n])
        print(ans)
    else:
        n, m = arg
        n -= 1
        m -= 1
        S[n].append(m)
        P[m] -= 1
