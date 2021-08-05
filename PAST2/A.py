# https://atcoder.jp/contests/past202004-open/tasks/past202004_a

base = ['B' + str(x) for x in range(9, 0, -1)]
ground = [str(x) + 'F' for x in range(1, 10)]
floor_list = base + ground

S, T = input().strip().split()

travel_time = abs(floor_list.index(S) - floor_list.index(T))

print(travel_time)
