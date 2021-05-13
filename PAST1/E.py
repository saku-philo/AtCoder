# https://atcoder.jp/contests/past201912-open/tasks/past201912_e

N, Q = map(int, input().split())

# False の N x N の2次元配列を作る
graph = []
for i in range(0, N):
    # 長さ N の False の1次元配列を作る
    row = []
    for i in range(0, N):
        row.append(False)

    # 作成した長さ N の False の1次元配列をgraphに追加する
    graph.append(row)

# Q個の操作を受け取る
for i in range(0, Q):
    query = list(map(int, input().split()))

    # 頂点番号は-1する
    a = query[1]-1

    # 1. フォロー
    if query[0] == 1:

        # 頂点番号は-1する
        b = query[2]-1

        # aからbへと辺を張る
        graph[a][b] = True

    # 2. フォロー全返し
    if query[0] == 2:

        # 全ての頂点を順番に見る。見ている頂点をvとする
        for v in range(0, N):
            # 頂点 v から頂点 a へと辺がある時
            if graph[v][a]:
                # 頂点 a から頂点 v へと辺を張る
                graph[a][v] = True

    # 3. フォローフォロー
    if query[0] == 3:

        # 頂点aから辺を貼る予定のリスト
        to_follow = []

        # 全ての頂点を順番に見る。見ている頂点をvとする
        for v in range(0, N):
            # 頂点aから頂点vへと向かう辺がある時
            if graph[a][v]:

                # さらに全ての頂点を順番に見る。見ている頂点をwとする
                for w in range(0, N):

                    # 頂点vから頂点wへと辺があり、かつwがaではない時
                    if graph[v][w] and w != a:
                        # 後で頂点aから辺を張るために記録する
                        to_follow.append(w)

        # 頂点aから辺を張る
        for w in to_follow:
            graph[a][w] = True

# 隣接行列を全て出力する
for i in range(0, N):
    for j in range(0, N):

        # iからjへと辺がある場合はYを、辺がない場合はNを出力する。改行はしない
        if graph[i][j]:
            print('Y', end='')
        else:
            print('N', end='')

    # N文字出力するごとに改行する
    print()
