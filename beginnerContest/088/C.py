# 3x3の２次元配列となる予定の配列
C = []

for _ in range(0, 3):
    # Cの１行分を表す１次元配列
    row = list(map(int, input().split()))

    C.append(row)

# 矛盾していないかを保持する変数
# 矛盾している場合 -> false
ok = True
