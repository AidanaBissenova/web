number =int(input())
i=0

while 2**i<=number:
    if(2**i==number):
        print("YES")
        break
    i+=1
else:
    print("NO")