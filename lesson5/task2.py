#task 2
a = e = i = o = u = even = odd = 0
print('enter the word')
word = input()
for letter in word:
    if letter == 'a': a += 1
    elif letter == 'e': e += 1
    elif letter == 'i': i += 1
    elif letter == 'o': o += 1
    elif letter == 'u': u += 1
    else: odd += 1
    even = a + e + i + o + u
print('even:', even)
print('odd:', odd)
print('a:', a)
print('e:', e)
print('i:', i)
print('o:', o)
print('u:', u)
