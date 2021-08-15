# https: // atcoder.jp/contests/abc088/tasks/abc088_b
N = int(input())

list = [int(i) for i in input().strip().split()]
list.sort(reverse=True)

Alice = []
Bob = []

for i in range(N):
    n = list.pop(0)

    if i % 2 == 0:
        Alice.append(n)
    else:
        Bob.append(n)

print(sum(Alice) - sum(Bob))
