# caeser cipher +K
caeser = {chr(i+65): i for  i in range(26)}
cipher = {i:chr(i+65) for i in range(26)}
s = list("HELLOWORLD")
K = 1
for i in range(len(s)):
    s[i] = cipher[(caeser[s[i]]+K)% 26]
print(''.join(s))
