# https://atcoder.jp/contests/past201912-open/tasks/past201912_c

def output_any_rank_from_list(rank, list):
    list.sort()
    return list[rank]

list = [int(i) for i in input().strip().split()]

rank = -3

ans = output_any_rank_from_list(rank, list)

print(ans)
