# https://atcoder.jp/contests/past202004-open/tasks/past202004_b

S = input().strip()

a = S.count('a')
b = S.count('b')
c = S.count('c')

m = max(a, b, c)

if m == a:
    print('a')
elif m == b:
    print('b')
else:
    print('c')
