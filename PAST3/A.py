S = input()
T = input()
lower_S = S.lower()
lower_T = T.lower()

ans = None

if (S == T):
    ans = "same"
elif (lower_S == lower_T):
    ans = "case-insensitive"
else:
    ans = "different"

print(ans)
