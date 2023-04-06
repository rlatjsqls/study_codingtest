from collections import deque

# 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 미로의 크기와 각 칸의 값을 입력받기
n, m = map(int, input().split())

maze = []
for i in range(n):
    maze.append(list(map(int, input().rstrip())))

# BFS 구현
def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    # 시작 칸을 방문 처리하기
    maze[x][y] = 1

    # 큐가 빌 때까지 반복하기
    while queue:
        x, y = queue.popleft()

        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 벽인 경우 무시
            if maze[nx][ny] == 0:
                continue

            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))

    # 가장 오른쪽 아래까지의 최단 거리 반환
    return maze[n-1][m-1]

# BFS를 수행한 결과 출력
print(bfs(0, 0))
