#6-10
#n개의 숫자를 내림차순으로 정렬하는 문제
#입력 예시
#3
#15
#27
#12
#출력예시
#27 15 12

n = int(input())

array = []
for i in range(n):
    array.append(int(input()))

array = sorted(array, reverse = True)

for i in array:
  print(i, end = ' ')

# for i in range(n):
#    print(array[i], end = ' ')
    
    
