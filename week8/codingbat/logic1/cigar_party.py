def cigar_party(c, w):
  if not w and c>=40 and c<=60 or w and c>=40:
    return True
  return False