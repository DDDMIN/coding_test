#7-5 부품찾기
#부품별 고유 번호가 있다. 고객이 요청한 부품이 있는지 확인하는 프로그램을 작성하자
#입력 예시
#보유 부품 수 N = 5
#보유 부품 고유 번호 [8, 3, 7, 9, 2]
#고객 요청 부품 수 M = 3
#고객 요청 부품 번호 [5, 7, 9]
#출력 예시
#no yes yes

#이진 탐색 소스코드
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)  #[1]
    else:
        return binary_search(array, target, mid + 1, end)

n = int(input())
array = list(map(int, input().split()))
array.sort()

m = int(input())
x = list(map(int, input().split()))


for i in x:
    #부품이 있는지 확인
    result = binary_search(array, i, 0, n - 1)
    if result != None:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')

#[1] 왜 여기 return 넣는걸 까먹을까? 값을 돌려줘야지 다음 계산을 하지...
