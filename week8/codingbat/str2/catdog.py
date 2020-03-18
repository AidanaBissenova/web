def catdog(str):
  count = 0
  sum = 0
  for i in range(len(str)-2):
    if str[i:i+3]=="cat":
      count+=1
    elif str[i:i+3]=="dog":
      sum+=1
  if count==sum:
    return True
  else:
    return False