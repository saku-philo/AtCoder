N = int(input())

# 既出のゾロ目数の数
z = 0

# 1~555555までの整数を全て調べる。調べている数を「i」とする
for i in range(1, 555555 + 1):
    # iを文字列に変換
    si = str(i)

    # ゾロ目判定変数
    ok = True

    # siの全ての文字列が「si」の0文字目と同じか確認
    # siの0文字目と違う文字が含まれている場合、iはゾロ目ではない
    for s in si:
        if s != si[0]:
            ok = False

    if ok:
        z += 1

    if ok and z == N:
        ans = i

print(ans)