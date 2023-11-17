#task 1
print('enter a number')
num = int(input())
message = ''
if num > 0: message += 'positive '
elif num < 0: message += 'negative '
else: message += 'zero '
if num == 0: message += ''
elif num % 2 == 0: message += 'even '
else: message += 'odd '
message += 'number'
print(message)