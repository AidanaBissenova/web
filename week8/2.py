a = int(input())
if a%2:
	print("Weird")
elif a%2==0 and  a >=1 and a <= 5:
	print("Not Weird")
elif a%2==0 and a>=6 and a<=20:
	print("Weird")
else:
	print("Not Weird")