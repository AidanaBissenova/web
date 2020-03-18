n = int(input())
sum=0
arr = [int(i) for i in input().split()]
for i in range(n):
	if arr[i] > 0: sum+=1
print(sum)
    
       