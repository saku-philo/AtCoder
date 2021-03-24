# ビンゴカードを表す配列
A = []

for _ in range(0, 3):
    # ビンゴカードの1行を受け取る(1次元配列)
    row = list(map(int, input().split()))

    # 受け取った1行分の配列をAの末尾に追加する
    # Aは1次元配列を要素とする配列のため、Aは2次元配列
    A.append(row)

# ビンゴカードの数字に印がついているか確認するカード（配列）
M = []
for i in range(0, 3):
    row = []
    for j in range(0, 3):
        row.append(False)

    M.append(row)


N = int(input())

# 選ばれた数字がカードに書かれているか判定
for _ in range(0, N):
    # 選ばれた数字
    b = int(input())

    # bがカードに書かれているか調べる
    for i in range(0, 3):
        for j in range(0, 3):
            if b == A[i][j]:
                # ビンゴカードのi行目j列に数字bがあれば、
                # M[i][j]=Trueとして印をつける
                M[i][j] = True

# ビンゴ達成かどうかを記録する変数
bingo = False

for i in range(0, 3):
    # i行目の3つに印がついているか調べる
    # 印がついていたらビンゴ達成
    if M[i][0] and M[i][1] and M[i][2]:
        bingo = True

for i in range(0, 3):
    # i列目の3つに印がついているか調べる
    # 印がついていたらビンゴ達成
    if M[0][i] and M[1][i] and M[2][i]:
        bingo = True

# 左上から右下にかけて、斜めに3つ印がついているか調べる
if M[0][0] and M[1][1] and M[2][2]:
    bingo = True

# 右上から左下にかけて、斜めに3つ印がついているか調べる
if M[0][2] and M[1][1] and M[2][0]:
    bingo = True

if bingo:
    print('Yes')
else:
    print('No')
