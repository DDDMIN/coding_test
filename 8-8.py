#n개의 화폐단위, m원의 목표 금액 설정
n, m = map(int, input().split())
#n개의 화폐 단위 정보를 입력받기
array = []
for i in range(n):
    array.append(int(input()))

d = [10001] * (m + 1)  #0원부터 m원까지 더미 생성

d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        if d[j - array[i]] != 10001:
            d[j] = min(d[j], d[j - array[i]] + 1)

if d[j] == 10001:
    print(-1)
else:
    print(d[m])
