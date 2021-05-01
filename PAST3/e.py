# https: // atcoder.jp/contests/past202005-open/tasks/past202005_e

N, M, Q = map(int, input().split())

# False の N × N の2元配列を作る
graph = []
for i in range(0, N):
    # 長さ N の False の1次元配列を作る
    row = []
    for j in range(0, N):
        row.append(False)

    # 長さ N の False の1次元配列を graph に追加
    graph.append(row)

# M 本の辺を受け取る
for i in range(0, M):
    u, v = map(int, input().split())

    # 頂点番号は全て-1する
    u -= 1
    v -= 1

    # uとvの間には辺があるためTrueにする
    graph[u][v] = True
    graph[v][u] = True

# 頂点の色のリストを受け取る
C = list(map(int, input().split()))

# Q個のクエリを受け取る
for i in range(0, Q):
    query = list(map(int, input().split()))

    # スプリンクラーを起動するクエリ
    if query[0] == 1:
        x = query[1]

        # 頂点番号は全てデクリメントする
        x -= 1

        # 頂点xの色を出力する
        print(C[x])

        #全ての頂点を順番に見る
        for i in range(0, N):
            # 頂点iが頂点xに隣接しているとき、
            # すなわち頂点xと頂点iの間に辺がある時
            if graph[x][i]:
                # 頂点iの色をC[x]に書き換える
                C[i] = C[x]

    # スプリンクラーを起動しないクエリの場合
    if query[0] == 2:
        x = query[1]
        y = query[2]

        # 頂点番号は全てデクリメントする
        x -= 1

        # 頂点xの色を出力する
        print(C[x])

        # 頂点xの色をyに書き換える
        C[x] = y
