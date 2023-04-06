import sys
sys.setrecursionlimit(10**9)

n = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [0] * (n+1)

def dfs(cur, prev):
    parent[cur] = prev
    for nxt in graph[cur]:
        if nxt != prev:
            dfs(nxt, cur)

dfs(1, 0)
for i in range(2, n+1):
    print(parent[i])


