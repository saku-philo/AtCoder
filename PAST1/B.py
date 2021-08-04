# https://atcoder.jp/contests/past201912-open/tasks/past201912_b

N = int(input())
Y = None
T = None

for i in range(0, N):
    if i == 0:
        Y = int(input())
        continue

    T = int(input())
    diff = T - Y
    val = str(abs(diff))

    if diff < 0:
        print('down ' + val)
    elif diff == 0:
        print('stay')
    else :
        print('up ' + val)

    Y = T
    T = None
