# https: // atcoder.jp/contests/arc046/tasks/arc046_a
import math

N = int(input())

# N番目のゾロ目数の桁数
x = math.ceil(N / 9)

# N番目のゾロ目の数字
y = N % 9

if y == 0:
    y = 9

# 回答文字列
ans = ""

for _ in range(0, x):
    ans += str(y)

print(ans)
