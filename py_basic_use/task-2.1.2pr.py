# вариант преподавателя
n = int(input())
classes = {}
for i in range(n):
    line = input()
    parts = line.split(" : ")
    cls = parts[0]
    if len(parts) == 1:
        classes[cls] = []
    else:
        classes[cls] = parts[1].split(" ")

def check(src, dest):
    if src == dest:
        return True
    return any([check(child, dest) for child in classes[src]])

m = int(input())
used = []

for i in range(m):
    cls = input()
    if any([check(cls, used_one) for used_one in used]):
        print(cls)
    used.append(cls)