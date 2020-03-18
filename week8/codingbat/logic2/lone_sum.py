def lone_sum(a, b, c):
  if a==c:
    return b
  elif a==b:
    return c
  elif c==b:
    return a
  elif a==b and b==c:
    return 0
  else:
    return a+b+c