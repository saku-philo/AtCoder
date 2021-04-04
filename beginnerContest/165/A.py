# https: // atcoder.jp/contests/abc165/tasks/abc165_a
K = int(input())

A, B = map(int, input().split())

# Kの倍数がA以上B以下の範囲内に存在するかを記録する変数
ok = False

# AからBまで順番に調べる 調べている変数をxとする
for x in range(A, B + 1):
    # 調べている数 x が K で割り切れるか調べる
    if x % K == 0:
        ok = True

# K で割り切れる数があれば OK を出力する
if ok:
    print("OK")
else:
    print("NG")
