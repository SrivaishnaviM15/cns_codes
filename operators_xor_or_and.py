# xor
s = list("hello world")
for i in range(len(s)):
    s[i] = chr(ord(s[i])^0)
print(''.join(s))

# or
s = list("hello world")
for i in range(len(s)):
    s[i] = chr(ord(s[i])|0)
print(''.join(s))

# and
s = list("hello world")
for i in range(len(s)):
    s[i] = chr(ord(s[i])&0)
print(''.join(s))
