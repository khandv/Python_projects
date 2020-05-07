import sys
sys.stdin = open("input3.txt", "r")

exceptions = {}
list_exceptions = []

def found_path(start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in exceptions:
        return []
    for node in exceptions[start]:
        if node not in path:
            newpath = found_path(node, end, path)
            if newpath: return newpath
    return []

for _ in range(int(input())):
    a = input().split()
    exceptions[a[0]] = a[2:]

for _ in range(int(input())):
    excs = input()
    for exc in list_exceptions:
        if len(found_path(excs, exc)) > 1:
            print(excs)
            break
    list_exceptions.append(excs)