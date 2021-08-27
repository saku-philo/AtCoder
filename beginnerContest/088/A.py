N = int(input())
A = int(input())

S = N % 500

ans = None

if S <= A:
    ans = 'Yes'
else:
    ans = 'No'

print(ans)
