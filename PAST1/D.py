# https: // atcoder.jp/contests/past201912-open/tasks/past201912_d

N = int(input().strip())
L = [0 for i in range(0, (N + 1))]
L[0] = None
ans = 'Correct'

# 整数xが整数yに書き換えられたとする
x = None
y = None

for j in range(0, N):
    num = int(input().strip())
    L[num] += 1

# 書き換えがあったかを判定
flag = L.count(2)
if flag:
    x = L.index(0)
    y = L.index(2)

if x and y:
    ans = '%d %d' % (y, x)

print(ans)
