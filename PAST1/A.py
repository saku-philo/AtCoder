# https://atcoder.jp/contests/past201912-open/tasks/past201912_a

def isInt(v):
  try:
    int(v, 10)
  except ValueError:
    return False
  else:
    return True

v = input()
o = 0

if (isInt(v)):
  v = int(v)
  o = 2 * v
else:
  o = "error"

print(o)
