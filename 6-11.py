#6-11
#n명의 학생에 대해 성적이 낮은 순서로 학생 출력하기
#입력예시
#2
#홍길동 95
#이순신 77
#출력예시
#이순신 홍길동


n = int(input())

array = []
for i in range(n):
    input_data = input().split()
    array.append(((input_data[0]), int(input_data[1]))) #[1]

array = sorted(array, key = lambda student : student[1]) #[2]

for student in array:
    print(student[0], end = ' ')



#[1] append 함수에는 input이 하나만 들어감. 그래서 input_data[0], input_data[1]을 하나로 묶어야함
#[2] sorted & lambda 참고
#출처 https://dailyheumsi.tistory.com/67
a = [(1, 2), (0, 1), (5, 1), (5, 2), (3, 0)]

# 인자없이 그냥 sorted()만 쓰면, 리스트 아이템의 각 요소 순서대로 정렬을 한다.
b = sorted(a)
# b = [(0, 1), (1, 2), (3, 0), (5, 1), (5, 2)]

# key 인자에 함수를 넘겨주면 해당 함수의 반환값을 비교하여 순서대로 정렬한다.
c = sorted(a, key = lambda x : x[0])
# c = [(0, 1), (1, 2), (3, 0), (5, 1), (5, 2)]
d = sorted(a, key = lambda x : x[1])
# d = [(3, 0), (0, 1), (5, 1), (1, 2), (5, 2)]

# 아이템 첫 번째 인자를 기준으로 오름차순으로 먼저 정렬하고,
# 그리고 그 안에서 다음 두 번째 인자를 기준으로 내림차순으로 정렬하게 하려면, 다음과 같이 할 수 있다.
e = [(1, 3), (0, 3), (1, 4), (1, 5), (0, 1), (2, 4)]
f = sorted(e, key = lambda x : (x[0], -x[1]))
# f = [(0, 3), (0, 1), (1, 5), (1, 4), (1, 3), (2, 4)]
