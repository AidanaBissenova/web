def make_choco(a, b, c):
  if (c>(a+b*5)) or ((c%5)>a):
    return -1
  elif b*5>c:
    return c%5 
  else:
    return c-b*5