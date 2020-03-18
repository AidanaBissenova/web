def make_bricks(a, b, c):
  if c > a + b * 5:
    return False
  else:
    return c % 5 <= a
        
  return False