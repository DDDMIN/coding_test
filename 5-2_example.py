
#5-8.py DFS 예제

def dfs(graph, v, visited):
    #현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:  #[1]
            dfs(graph, i, visited)

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9  #[2]

dfs(graph, 1, visited)


#5-9 BFS 예제
from collections import deque

#BFS method 정의
def bfs(graph, start, visited):
    #queue 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        #queue에서 하나의 원소를 뽑아 출력(맨앞에 있는거)
        v = queue.popleft()
        print(v, end = ' ')
        #해당 원소와 연결되고 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

#정의된 BFS 함수 호출
bfs(graph, 1, visited)

#각주
#[1] if not ~ : ~이 False 일때 실행
#[2] 뒤에서 호출해주기 때문에 더미로 visited 정보 List 생성함
