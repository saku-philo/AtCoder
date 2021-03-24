# 標準入力から文字列を受け取る
S = input()

# 文字a, b, cの個数をそれぞれ数える
na = S.count("a")
nb = S.count("b")
nc = S.count("c")

# 一番多い文字を調べて出力する
mx = max(na, nb, nc)
if na == mx:
    print("a")
elif nb == mx:
    print("b")
elif nc == mx:
    print("c")
