number = int(input())
arr = list(map(int, input().split()))

for i in range(0, int(number/2)):
    temp = arr[i]
    arr[i] = arr[number - i - 1]
    arr[number - i - 1] = temp

for i in range (0, number):
    print(arr[i], end = ' ')