s = input()
x = len(s)
ans = 0

for i in range(1 << x-1):
    prev = 0
    for j in range(x):
        if(j == x-1 or i >> j & 1):
            ans += int(s[prev:j+1])
            prev = j+1

print(ans)
