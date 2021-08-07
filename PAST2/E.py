def counter(i, int_list):
    index = i - 1
    A = int_list[index]
    count = 1

    while i != A:
        index = A - 1
        A = int_list[index]
        count += 1

    return count

N = int(input().strip())

list = [int(i) for i in input().strip().split()]

ans = []

for i in range(1, (N + 1)):
    res = counter(i, list)
    ans.append(res)

# 数値要素リストを結合して出力
print(' '.join(map(str, ans)))
