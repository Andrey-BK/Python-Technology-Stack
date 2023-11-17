#task 1
str = input()
reverse = str[len(str):0:-1] + str[0]
if reverse == str: print('yes')
else: print('no')