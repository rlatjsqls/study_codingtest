import sys
from collections import deque

result = {}

def bfs(x, root):
    global result
    q = deque()
    q.append(x)
    while q:
        a = q.popleft()
        if a == 1:
            for i in root[a]:
                q.append(i)
            result[a] = 0
        else:
            for i in root[a]:
                if i in result:
                    result[a] = i
                else:
                    q.append(i)

root = {}
n = int(input())
for _ in range(n-1):
    i, j = list(map(int,sys.stdin.readline().split()))
    if i not in root:
            root[i] = [j]
    else:
        root[i].append(j)
    if j not in root:
        root[j] = [i]
    else:
        root[j].append(i)
print(root)

bfs(1, root)
for i in range(2,n+1):
    print(result[i])