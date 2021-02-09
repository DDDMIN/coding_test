#5-1 스택 예제
#선입 후출 First In Last Out
stack = []
#삽입(5) 삽입(2) 삽입(3) 삽입(7) 삭제() 삽입(1) 삽입(4) 삭제()
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)    #최하단 원소부터 출력
print(stack[::-1]) #최상단 원소부터 출력
#결과
#[5, 2, 3, 1]
#[1, 3, 2, 5]

#5-2
#큐 Queue 선입선출 First In First Out
#queue 구성을 위해 deque 라이브러리 사용
from collections import deque

queue = deque() 

#삽입(5) 삽입(2) 삽입(3) 삽입(7) 삭제() 삽입(1) 삽입(4) 삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)

#결과
#deque([3, 7, 1, 4])
#deque([4, 1, 7, 3])


#5-5 Factorial 예제

#반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1
    for i in range(1, n):
        result *= i
    return result

#재귀적으로 구현한 n!
def factorial_recursive(n):
    #재귀함수가 무한히 반복하는것을 막기 위해 1 이하의 경우에 대해 값을 정해줌
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

print('반복적으로 구현', factorial_iterative(5))
print('재귀적으로 구현', factorial_recursive(5))

#결과
#반복적으로 구현 0
#재귀적으로 구현 120


