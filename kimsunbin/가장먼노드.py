from collections import deque

result = {}

def bfs(x, root):
    global result
    q = deque()
    q.append([x,0])
    while q:
        a,b = q.popleft()
        if a not in result:
            result[a] = b
        else:
            continue
        for i in root[a]:
            if i not in result:
                q.append([i,b+1])
def solution(n, edge):
    root = {}

    #edge.sort(key = lambda x : x[0])

    for i, j in edge:
        if i not in root:
            root[i] = [j]
        else:
            root[i].append(j)
        if j not in root:
            root[j] = [i]
        else:
            root[j].append(i)
    bfs(1, root)
    m = max(result.values())
    cnt = 0
    for i in result:
        if m == result[i]:
            cnt += 1
    return cnt