#task 2
print('enter a number N')
n = int(input())
print('enter N numbers separated by a space')
arr = list(map(int, input().split()))
for i in range(n, 1, -1):
    mem = arr[i-1]
    arr[i-1] = arr[i-2]
    arr[i-2] = mem
print(arr)