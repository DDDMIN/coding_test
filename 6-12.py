#6-12 두 배열의 원소교체
#n개의 원소로 이루어진 두개의 배열에 대해 k번 바꿔치기함
#이때 a배열의 원소의 합의 최댓값은?
#입력 예시
# 5 3
# 1 2 5 4 3
# 5 5 6 6 3
#출력 예시
# 26

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse = True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i] #[1]
    else:
        break

print(sum(a))


#[1]  a[i], b[i] = b[i], a[i] 바꾸기
