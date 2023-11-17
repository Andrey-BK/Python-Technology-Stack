#task 2
print('enter a number')
num = int(input())
count = 0
for i in range(num, 0, -1):
    if num % i: count += 1
print(count)