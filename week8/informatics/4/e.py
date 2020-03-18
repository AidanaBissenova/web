n = int(input())
arr = input() 
l = list(map(int,arr.split(' ')))

c = False

for i in range (0,n-1):
    if (l[i+1] > 0 and l[i] > 0) or (l[i+1] < 0 and l[i] < 0):
       c = True
       
if c == False:
    print("NO")

if c == True:
    print("YES") 