list = list(map(int, input().split()))
set = set()
for i in list:
    mem = i in set
    print(i, mem)
    set.add(i)
