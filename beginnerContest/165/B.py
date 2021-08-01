# https://atcoder.jp/contests/abc165/tasks/abc165_b

# 目標金額
X = int(input())

# 初期貯金額
Y = 100

# 年数
Z = 0

while Y < X:
  Y += Y // 100
  Z += 1

print(Z)
