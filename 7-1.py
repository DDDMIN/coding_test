#7-1 순차 탐색 소스코드

def sequential_search(n, target, array):
    for i in range(n):
        #현재의 원소가 찾고자 하는 원소와 동일한 경우
        if array[i] == target:
            return i + 1

print('type number of element + space + target element')
input_data = input().split()
n = int(input_data[0])
target = input_data[1]

print('input elements')
array = input().split()

#결과 출력
print(sequential_search(n, target, array))

