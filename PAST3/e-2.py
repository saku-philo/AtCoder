# https: // atcoder.jp/contests/past202005-open/tasks/past202005_e
# 隣接リスト解法

N, M, Q = map(int, input().split())

# N × 0 の2元配列を作る
graph = []
for i in range(0, N):
    # 長さ 0 の 1次元配列を作る
    row = []
    graph.append(row)

# M 本の辺を受け取る
for i in range(0, M):
    u, v = map(int, input().split())

    # 頂点番号は全て-1する
    u -= 1
    v -= 1

    # 頂点 u から v へ辺がある
    graph[u].append(v)

    # 頂点 v から u へ辺がある
    graph[v].append(u)


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

        # 頂点 x に隣接する頂点の色を頂点 x と同じ色にする
        for i in graph[x]:
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
