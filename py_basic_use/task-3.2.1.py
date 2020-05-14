s = input()
a = input()
b = input()

n = 0
while n < 1000:
    if a in s:
        s = s.replace(a, b)
        n += 1
    else: break

print(n if n < 1000 else 'Impossible')
