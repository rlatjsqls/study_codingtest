n, m = map(int,(input().split()))
maps = [[0 for i in range(m)]for j in range(n)]
for i in range(n):
    x = input()
    for j, y in enumerate(x):
        maps[i][j] = int(y)

from collections import deque

def bfs(y, x):
    q = deque()
    q.append((y, x, 1))

    while q:
        y, x, distance = q.popleft()

        if y == len(maps)-1 and x == len(maps[0])-1:
            return distance

        if maps[y][x] == 0:
            continue
        maps[y][x] = 0

        if y+1 < len(maps):
            q.append((y+1, x, distance+1))
        if x+1 < len(maps[0]):
            q.append((y, x+1, distance+1))
        if y-1 >= 0:
            q.append((y-1, x, distance+1))
        if x-1 >= 0:
            q.append((y, x-1, distance+1))

    return -1

print(bfs(0,0))