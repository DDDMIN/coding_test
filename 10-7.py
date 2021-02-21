#특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

#두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
        parent[a] = b

n, m = map(int, input().split())
parent = [0] * (n + 1)

for i in range(0, n + 1):
    parent[i] = i

#각 연산을 하나씩 확인
for i in range(m):
    oper, a, b = map(int, input().split())
    #합집합 연산인 경우
    if oper == 0:
        union_parent(parent, a, b)
    #찾기 연산인 경우
    if oper == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')
        else:
            print('NO')
            
    
