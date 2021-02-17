#9-4 1번에서 K번 회사 거쳤다 X번 회사 방문

INF = int(1e9)
#회사의 개수 N과 경로의 개수 M 입력
n, m = map(int, input().split())
#2차원 리스트를 만들고 모든값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

#자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

#각 간선에 대한 정보를 입력받아 그 값으로 초기화
for _ in range(m):
    a, b = map(int, input().split())
    #문제에서 경로의 비용은 모두 1이었음
    graph[a][b] = 1
    graph[b][a] = 1

# 목적지 x와 거처갈 회사 k 입력
x, k = map(int, input().split())

#플로이드 워설 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

#수행된 결과를 출력
distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print('-1')
else:
    print(distance)
