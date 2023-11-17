print('enter the dictionary keys separated by a space')
keys = list(map(int, input().split()))
my_dict = {}
for i in keys:
    my_dict[i] = i ** i
print(my_dict)