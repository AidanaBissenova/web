from math import sqrt
number=int(input())
count=0

for x in range(1, int(sqrt(number))):
    if(number%x==0):
        count+=1

count*=2
if number%int(sqrt(number))==0: count+=1
print(count)