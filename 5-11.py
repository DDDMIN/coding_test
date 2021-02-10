#5-11 미로 탈출문제
#n행 * m열의 미로. 시작위치는 1,1 도착위치는 n,m
#괴물이 있는 부분은 0, 괴물이 없는 부분은 1
#탈출하기 위해 움직여야 하는 최소 칸의 개수는?(처음, 마지막칸 포함)

from collections import deque

#n행 m열
n, m = map(int, input().split())
#2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

#이동할 방향(상 하 좌 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#BFS 소스코드 구현
def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    #큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #구역을 벗어난 경우 정지
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            #괴물이 있는경우 안간다
            if graph[nx][ny] == 0:
                continue
            #해당 노드를 처음 가는 경우에만 최단거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    #[1] 들여쓰기를 잘못함;; return 한칸 더 들여써서 값이 이상하게 나옴
    return graph[n-1][m-1]

print(bfs(0, 0))
