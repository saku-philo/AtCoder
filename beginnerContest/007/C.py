from collections import deque

R, C = list(map(int, input().split()))
sy, sx = list(map(int, input().split()))
gy, gx = list(map(int, input().split()))
S = []

for i in range(R):
    s = input()
    S.append(s)

# 始点と終点を0始まりに直す
sy -= 1
sx -= 1
gy -= 1
gx -= 1

# 始点からの最小移動回数を管理する2次元配列、-1であれば未訪問
dist = []
for i in range(R):
    dist.append([-1]*C)

# キューを用意して始点を入れる
Q = deque()
Q.append([sy, sx])
dist[sy][sx] = 0

# キューから頂点を取り出しながら探索する
while len(Q) > 0:
    i, j = Q.popleft()
    # 隣接する4つのマスを確認
    for i2, j2 in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
        # 盤面の範囲外なら無視する
        if not (0 <= i2 < R and 0 <= j2 < C):
            continue
        # 壁マスなら無視する
        if S[i2][j2] == '#':
            continue
        # もし未訪問であれば(dist[i2][j2]が-1)であれば、距離を更新してキューに入れる
        if dist[i2][j2] == -1:
            dist[i2][j2] = dist[i][j] + 1
            Q.append([i2, j2])

# 始点から終点までの最小移動回数を出力
print(dist[gy][gx])
