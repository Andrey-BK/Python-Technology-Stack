print('enter the length of the first list')
len1 = int(input())
print('enter the first list')
set1 = set()
for i in range(len1):
    set1.add(int(input()))

print('enter the length of the second list')
len2 = int(input())
print('enter the second list')
set2 = set()
for i in range(len2):
    set2.add(int(input()))

print(len(set1.intersection(set2)))