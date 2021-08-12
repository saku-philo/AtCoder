N = int(input())
C = list(map(int, input().split()))
Q = int(input())

# 販売合計
sell = 0

# 全種類販売した1種類の枚数
z = 0

# セット販売した1種類の枚数
s = 0

# セット販売対象のC最小値記録変数
min_s_C = 1000000000

# セット販売対象外のC最小値記録変数
min_z_C = 1000000000

# indexは0からスタートのため、奇数番号カード = 割り切れるindex
for i in range(0, N):
    if i % 2 == 0:
        min_s_C = min(C[i], min_s_C)
    else:
        min_z_C = min(C[i], min_z_C)

# クエリ処理
for _ in range(0, Q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        # 単品販売
        x = query[1] - 1
        a = query[2]

        # カードxの残枚数を計算
        if x % 2 == 0:
            # セット販売対象
            card_x = C[x] - z - s
        else:
            # セット販売対象外
            card_x = C[x] - z

        # カードxがa枚以上残っていればa枚売る
        if card_x >= a:
            C[x] -= a
            sell += a

            if x % 2 == 0:
                min_s_C = min(C[x], min_s_C)
            else:
                min_z_C = min(C[x], min_z_C)

    elif query[0] == 2:
        # セット販売
        a = query[1]

        # i%2==0となるC[i]の最小値について、カードがa枚以上あるか調べる
        # a枚以上の場合、a枚ずつ売る
        if min_s_C - s - z >= a:
            s += a

    elif query[0] == 3:
        # 全種類販売の場合
        a = query[1]

        # Cの最小値について、そのカードがa枚以上あるか調べる
        # a枚以上の場合、a枚ずつ売る
        if min(min_s_C - s - z, min_z_C - z) >= a:
            z += a

# セット販売した枚数を合算する
for i in range(0, N):
    if i % 2 == 0:
        sell += s

# 全種類販売した枚数を合算する
sell += z * N

print(sell)
