#7-2 이진탐색 코드

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    #mid = target 일경우
    if array[mid] == target:
        return mid
    #mid < target일 경우
    if array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    #mid > target일 경우
    else:
        return binary_search(array, target, mid + 1, end)

n, target = map(int, input().split())
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n -1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
