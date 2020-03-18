import math
a = int(input())
i=0
if a > 0:	
	while(i<a):
		i+=1
		if math.floor(math.sqrt(i)) == math.sqrt(i):
			print (i,' ') 
