s = input()
t = input()

n = 0
for i in range(len(s)-len(t)+1):
    if s[i:].startswith(t):
        n += 1

print(n)