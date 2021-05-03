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

graph[a][b] = True

# 全ての頂点を順番に見る。見ている頂点をvとする
for v in range(0, N):
    # 頂点 v から頂点 a へと辺がある時
    if graph[v][a]:
        # 頂点 a から頂点 v へと辺を張る
        graph[a][v] = True

# for v in range(0, N):
