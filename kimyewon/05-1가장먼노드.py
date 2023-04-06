'''
1번 노드에서 가장 멀리 떨어지 ㄴ노드의 개수 => 최단경로 이동시 간선의 개수가 가장 많은 노드


'''
from collections import deque

def solution(n, edge):

    ## 입력 받은 데이터로 그래프 만들기
    graph = [[] for _ in range(n+1)]

    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    print(graph)
    ## 1번 노드와 거리를 기록할 리스트
    distance = [0] * (n+1)
    distance[1] = 1
    queue = deque([1]) # 1 번 노드에서 시작

    ## Q 가 비어질때까지 반복문을 돌린다

    while queue:
        src = queue.popleft() #
        for dest in graph[src]:

            if distance[dest] == 0:
                queue.append(dest)
                distance[dest] = distance[src] + 1

    return distance.count(max(distance))

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))