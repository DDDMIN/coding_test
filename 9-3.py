#9-3 플로이드 워셜 알고리즘 소스코드
INF = int(1e9) #무한을 의미하는 값으로 10억을 설정

#노드의 개수 및 간선의 개수를 입력하기
n = int(input())
m = int(input())
#2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

#자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 수행된 결과를 출력
for a in range(1, n + 1):
    for b in range(1, b + 1):
        if graph[a][b] == INF:
            print("INF", end = " ")
        else:
            print(graph[a][b], end = " ")
    print()
